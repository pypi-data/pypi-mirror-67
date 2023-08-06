# (c) 2012-2018 Dativa, all rights reserved
# -----------------------------------------
#  This code is licensed under MIT license (see license.txt for details)

from csv import QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE
import logging
from io import StringIO, BytesIO
from csv import Sniffer, Error
from dativa.tools.aws import S3Location, S3ClientError
from functools import wraps
import os
import gzip
import zipfile
import warnings

try:
    from awsretry import AWSRetry
except ImportError:
    class AWSRetry:
        @classmethod
        def backoff(cls, *_, **__):
            def decorator(f):
                @wraps(f)
                def wrapper(*args, **kwargs):
                    return f(*args, **kwargs)

                return wrapper

            return decorator

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import s3fs
except ImportError:
    s3fs = None

try:
    from chardet.universaldetector import UniversalDetector
except ImportError:
    UniversalDetector = None

try:
    from Crypto.Cipher import AES
except ImportError:
    AES = None

logger = logging.getLogger("dativa.tools.pandas.csv")


class FpCSVEncodingError(Exception):
    def __init__(self, message="CSV Encoding Error"):
        self.message = message


class CSVHandler:
    """
    A wrapper for pandas CSV handling to read and write dataframes
    that is provided in pandas with consistent CSV parameters and
    sniffing the CSV parameters automatically.
    Includes reading a CSV into a dataframe, and writing it out to a string.

    Parameters
    ----------
    base_path: the base path for any CSV file read, if passed as a string
    detect_parameters: whether the encoding of the CSV file should be automatically detected
    encoding: the encoding of the CSV files, defaults to UTF-8
    delimiter: the delimeter used in the CSV, defaults to ,
    header: the index of the header row, or -1 if there is no header
    skiprows: the number of rows at the beginning of file to skip
    usecols: which columns to read from the CSV
    quotechar: the quoting character to use, defaults to ""
    include_index: specifies whether the index should be written out, default to False
    compression: specifies whether the data should be encoded, default to 'infer'
    nan_values: an array of possible NaN values, the first of which is used when writing out, defaults to None
    line_terminator: the line terminator to be used
    quoting: the level of quoting, defaults to QUOTE_MINIMAL
    decimal: the decimal character, defaults to '.'
    chunksize: if specified the CSV is written out in chunks
    aes_key: the public key for encryption while writing out files, length must be multiple of 16 - default to None
    aes_iv: the private key for reading in encrypted files, length must be 16 - default to None
    :type aes_key bytes
    :type aes_iv bytes
    """

    base_path = ""
    DEFAULT_ENCODING = "UTF-8"
    DEFAULT_DELIMITER = ","
    DEFAULT_HEADER = 0
    DEFAULT_QUOTECHAR = "\""
    S3_PREFIX = "s3://"
    SAMPLE_SIZE = 1024 * 1024

    allowed_read_compression = {'gzip', 'bz2', 'zip', 'xz', None, 'infer'}
    allowed_quote_levels = {QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE}
    allowed_zipfile_compressions = {zipfile.ZIP_DEFLATED, zipfile.ZIP_STORED, zipfile.ZIP_BZIP2, zipfile.ZIP_LZMA}
    allowed_write_compressions = {'gzip', 'infer', 'zip'}

    detect_parameters = False
    include_index = False
    compression = 'infer'
    nan_values = None
    line_terminator = None
    quoting = QUOTE_MINIMAL
    decimal = '.'
    chunksize = None
    nrows = None
    encoding = DEFAULT_ENCODING
    force_dtype = None
    delimiter = DEFAULT_DELIMITER
    header = DEFAULT_HEADER
    s3c = None
    skiprows = 0
    usecols = None
    quotechar = DEFAULT_QUOTECHAR
    aes_key = None
    aes_iv = None
    s3c_kwargs = {}
    pd_kwargs = {}
    zipfile_compression = zipfile.ZIP_DEFLATED

    def __init__(self,
                 **kwargs):

        if not pd:
            raise ImportError("pandas must be installed to run CSVHandler")

        if s3fs is None:
            self.s3fs_version_number = 0
        else:
            self.s3fs_version_number = int(s3fs.__version__.split('.')[1]) if int(
                s3fs.__version__.split('.')[0]) == 0 else 3
            if self.s3fs_version_number >= 3:
                warnings.warn('You are using version {} of s3fs it is recommended to use 0.1.5 =< s3fs <0.3.0.'.format(
                    s3fs.__version__))

        self._process_kwargs(**kwargs)

        # validate if base path is a folder and exists
        # support file like objects

    def value_or_default(self, args, name):
        if name in args:
            setattr(self, name, args[name])
        elif "csv_{0}".format(name) in args:
            setattr(self, name, args["csv_{0}".format(name)])

    def _process_kwargs(self, **kwargs):

        self.value_or_default(kwargs, "aes_key")
        self.value_or_default(kwargs, "aes_iv")
        self.value_or_default(kwargs, "base_path")
        self.value_or_default(kwargs, "chunksize")
        self.value_or_default(kwargs, "compression")
        self.value_or_default(kwargs, "decimal")
        self.value_or_default(kwargs, "delimiter")
        self.value_or_default(kwargs, "detect_parameters")
        self.value_or_default(kwargs, "encoding")
        self.value_or_default(kwargs, "force_dtype")
        self.value_or_default(kwargs, "header")
        self.value_or_default(kwargs, "include_index")
        self.value_or_default(kwargs, "line_terminator")
        self.value_or_default(kwargs, "nan_values")
        self.value_or_default(kwargs, "pd_kwargs")
        self.value_or_default(kwargs, "quotechar")
        self.value_or_default(kwargs, "quoting")
        self.value_or_default(kwargs, "s3c")
        self.value_or_default(kwargs, "s3c_kwargs")
        self.value_or_default(kwargs, "skiprows")
        self.value_or_default(kwargs, "usecols")
        self.value_or_default(kwargs, "names")
        self.value_or_default(kwargs, 'nrows')
        self.value_or_default(kwargs, 'zipfile_compression')

        if self.compression not in self.allowed_read_compression:
            raise ValueError("Invalid value for compression parameter")

        if self.quoting not in self.allowed_quote_levels:
            raise ValueError("Invalid value for quoting parameter")

        if self.zipfile_compression not in self.allowed_zipfile_compressions:
            raise ValueError("Invalid zip compression parameter")

        if self.aes_iv and not self.aes_key:
            raise ValueError("Cannot specify an aes_iv without an aes_key")

        if self.aes_key and self.detect_parameters:
            raise NotImplementedError("Cannot yet specify detect_parameters and encryption simultaneously"
                                      " - must specify encoding if not UTF-8")

        if self.aes_key:
            if not AES:
                raise ImportError("Pycryptodomo must be installed to use an AES key")

            # initialise a cipher to make sure the key and (if provided) IV are valid
            AES.new(self.aes_key, AES.MODE_CFB, self.aes_iv)

        if self.detect_parameters:
            if not UniversalDetector:
                raise ImportError("chardet must be installed to use detect_parameters in dativa.tools CSVHandler")

        if self.line_terminator is None:
            self.line_terminator = os.linesep

    @property
    def s3_client(self):
        if not self.s3c:
            try:
                import boto3
            except ImportError:
                raise ImportError("boto3 must be installed to use S3 URLs")

            self.s3c = boto3.client("s3", **self.s3c_kwargs)

        return self.s3c

    @property
    def _has_header(self):
        """
        Returns whether the CSV file has a header or not
        """
        if self.header == -1:
            return False
        else:
            return True

    @property
    def _default_nan(self):
        if self.nan_values is None:
            return ''
        else:
            return self.nan_values[0]

    def _is_s3_file(self, full_path):

        if full_path.startswith(self.S3_PREFIX):
            try:
                S3Location(full_path)
                return True
            except S3ClientError:
                pass

        return False

    def _get_file(self, file):
        return os.path.join(self.base_path, file)

    def _get_df_from_raw(self, file):
        """
        Returns a DataFrame from a passed file
        """

        file_or_buffer = self._get_file(file)
        if self.aes_key:
            # load file to buffer as appropriate
            if self._is_s3_file(file_or_buffer):
                loc = S3Location(file_or_buffer)
                buffer = self.s3read_with_retries(bucket=loc.bucket, key=loc.key)
            else:  # treat as local file
                with open(file_or_buffer, "rb") as f:
                    buffer = f.read()

            # determine the iv
            if self.aes_iv:
                iv, encrypted_bytes = self.aes_iv, buffer
            else:
                # assume prepended randomised iv
                iv, encrypted_bytes = buffer[:AES.block_size], buffer[AES.block_size:]

            # then decrypt,
            cipher = AES.new(self.aes_key, AES.MODE_CFB, iv=iv)
            decrypted_bytes = cipher.decrypt(encrypted_bytes)
            # then apply appropriate encoding to convert byte to str
            file_or_buffer = StringIO(decrypted_bytes.decode(self.encoding))

        elif self._is_s3_file(file_or_buffer):
            self._assert_s3_key_exists_with_retries(file_or_buffer)
        try:
            df = pd.read_csv(file_or_buffer,
                             encoding=self.encoding,
                             sep=self.delimiter,
                             quotechar=self.quotechar,
                             header=self.header if self._has_header else None,
                             skiprows=self.skiprows,
                             usecols=self.usecols,
                             skip_blank_lines=False,
                             dtype=self.force_dtype,
                             compression=self.compression,
                             na_values=self.nan_values,
                             lineterminator=self.line_terminator,
                             quoting=self.quoting,
                             decimal=self.decimal,
                             chunksize=self.chunksize,
                             nrows=self.nrows,
                             **self.pd_kwargs)
        except EOFError as e:
            if self.s3fs_version_number >= 3:
                raise type(e)(
                    e.message +
                    'This error can be caused by a bug in s3fs version 3 and above if compression is specified')
            else:
                raise e

        return df

    @staticmethod
    def _get_encoding(sample):
        detector = UniversalDetector()
        for line in BytesIO(sample).readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result["encoding"]

    def _sniff_parameters(self, file):
        """
        sets instance variable with detected parameters from file
        :param file: name of file to be considered (relative to self.base_path)
        :return: True if able to detect parameters
        """
        # if we are using the default parameters, then attempt to guess them
        if (self.encoding == self.DEFAULT_ENCODING and
                self.delimiter == self.DEFAULT_DELIMITER and
                self.header == self.DEFAULT_HEADER and
                self.quotechar == self.DEFAULT_QUOTECHAR):
            logger.debug("sniffing file type")

            # create a sample...
            full_path = self._get_file(file)
            if full_path.startswith(self.S3_PREFIX):
                # This is an S3 location
                loc = S3Location(full_path)
                logger.debug("s3 location: {}".format(loc))
                sample = self.s3read_with_retries(bucket=loc.bucket, key=loc.key, size=self.SAMPLE_SIZE)
            else:
                with open(full_path, mode="rb") as f:
                    sample = f.read(self.SAMPLE_SIZE)

            # get the encoding...
            self.encoding = self._get_encoding(sample)
            if self.encoding is None:
                self.encoding = 'windows-1252'

            # now decode the sample
            try:
                sample = sample.decode(self.encoding)
            except UnicodeDecodeError:
                self.encoding = "windows-1252"
                try:
                    sample = sample.decode(self.encoding)
                except UnicodeDecodeError as e:
                    raise FpCSVEncodingError(str(e))

            # use the sniffer to detect the parameters...
            sniffer = Sniffer()
            try:
                dialect = sniffer.sniff(sample)
            except Error as e:
                raise FpCSVEncodingError(str(e))

            self.delimiter = dialect.delimiter
            # the detector always seems to find a header... below line is in case it does not
            self.header = 0 if sniffer.has_header(sample) else -1
            self.quotechar = dialect.quotechar

            if (self.encoding != self.DEFAULT_ENCODING or
                    self.delimiter != self.DEFAULT_DELIMITER or
                    self.header != self.DEFAULT_HEADER or
                    self.quotechar != self.DEFAULT_QUOTECHAR):
                logger.debug("Found file type {0}, delimiter {1}, header {2}, quotechar {3}".format(
                    self.encoding, self.delimiter, self.header, self.quotechar))
                return True

        logger.warning("No new file type found while sniffing parameters.")
        return False

    def _attempt_get_df_from_raw(self, file):
        try:
            return self._get_df_from_raw(file)
        except (UnicodeError, UnicodeDecodeError, pd.errors.ParserError) as e:
            err_msg = str(e)
            if self.detect_parameters:
                if not self.aes_key and self._sniff_parameters(file):
                    logger.debug("second attempt to load")
                    return self._get_df_from_raw(file)
            if type(e) is UnicodeDecodeError:
                err_msg += ". This file may be encrypted, which would require the decryption key and iv for the file."
            raise FpCSVEncodingError(err_msg)

    @AWSRetry.backoff()
    def s3read_with_retries(self, bucket, key, size=None):
        obj = self.s3_client.get_object(Bucket=bucket, Key=key)
        return obj["Body"].read(size)

    @AWSRetry.backoff(tries=10, delay=1, backoff=1, added_exceptions=['404'])
    def _assert_s3_key_exists_with_retries(self, file):
        s3loc = S3Location(file)
        self.s3_client.head_object(Bucket=s3loc.bucket, Key=s3loc.key)

    def load_df(self, file, **kwargs):
        """
        Synonym for 'get_dataframe' for consistency with 'save_df'
        """
        return self.get_dataframe(file, **kwargs)

    def get_dataframe(self, file, **kwargs):
        """
        Opens a CSV file using the specified configuration for the class
        and raises an exception if the encoding is unparseable
        """
        self._process_kwargs(**kwargs)

        df = self._attempt_get_df_from_raw(file)

        return df

    def _get_csv_bytes(self, df, file):
        if self.compression not in self.allowed_write_compressions:
            raise ValueError("Only gzip or zip compression is supported for writing dataframes")

        if self.compression == 'gzip':
            buffer = BytesIO()
            with gzip.open(buffer, 'wb') as f:
                f.write(self._get_csv(df).encode(self.encoding))

            buffer.seek(0)
            return buffer.getvalue()

        elif self.compression == 'zip':
            file_name = file.rsplit('/')[-1]
            file_name_no_extension = file_name.rsplit('.', 1)[0] if file_name.endswith('.zip') else file_name
            csv_file_name = file_name_no_extension + '.csv'
            buffer = BytesIO()
            with zipfile.ZipFile(buffer, 'w', compression=self.zipfile_compression) as f:
                f.writestr(csv_file_name, self._get_csv(df).encode(self.encoding))

            buffer.seek(0)
            return buffer.getvalue()

        else:
            return self._get_csv(df).encode(self.encoding)

    def _get_csv(self, df):

        buffer = StringIO()

        df.to_csv(buffer,
                  encoding=self.encoding,
                  sep=self.delimiter,
                  quotechar=self.quotechar,
                  header=self._has_header,
                  index=self.include_index,
                  na_rep=self._default_nan,
                  line_terminator=self.line_terminator,
                  quoting=self.quoting,
                  decimal=self.decimal,
                  chunksize=self.chunksize
                  )

        buffer.seek(0)
        return buffer.getvalue()

    def save_df(self, df, file, **kwargs):
        """
        Writes a formatted string from a DataFrame using the specified
        configuration for the class the file. Detects if base_path is
        an S3 location and saves data there if required. Handles encryption

        """

        self._process_kwargs(**kwargs)

        bytes_to_write = self._get_csv_bytes(df, file)
        if self.aes_key:
            if not AES:
                raise ValueError("Pycryptodomo is required to use an aes_key")

            cipher = AES.new(self.aes_key, AES.MODE_CFB, self.aes_iv)
            # I assume this will need a lot of memory - it passes a copy back rather than operating in place
            if self.aes_iv:
                bytes_to_write = cipher.encrypt(bytes_to_write)
            else:
                bytes_to_write = cipher.iv + cipher.encrypt(bytes_to_write)

        path = self._get_file(file)
        if self._is_s3_file(path):
            # Save buffered data to file in S3 bucket
            loc = S3Location(path)
            self.s3_client.put_object(Bucket=loc.bucket,
                                      Key=loc.key,
                                      ContentEncoding=self.encoding,
                                      ContentType="text/csv",
                                      Body=bytes_to_write)
        else:
            with open(self._get_file(file), "wb") as f:
                f.write(bytes_to_write)

    def df_to_string(self, df, **kwargs):
        """
        Returns a formatted string from a dataframe using the specified
        configuration for the class
        """

        self._process_kwargs(**kwargs)

        return self._get_csv(df)
