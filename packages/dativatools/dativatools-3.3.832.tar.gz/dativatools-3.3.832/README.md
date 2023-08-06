# Dativa Tools

Provides useful libraries for processing large data sets. 
Developed by the team at [www.dativa.com](https://www.dativa.com) as we find them useful in our projects.

The key libraries included here are:

* dativa.tools.aws.S3Csv2Parquet - an AWS Glue based tool to transform CSV files to Parquet files
* dativa.tools.aws.AthenaClient - provide a simple wrapper to execute Athena queries and create tables. When combined 
with the S3Csv2Parquet handler can automatically change Athena outputs to Parquet format
* dativa.tools.aws.PipelineClient - client to interact with the Pipeline API. When provided an api key, source S3 
location, destination s3 location, and rules, it will clean the source file and post it to destination.
* dativa.tools.aws.S3Client - a wrapper for AWS's boto library for S3 enabling easier iteration over S3 files and 
multiple deletions, as well as uploading multiple files
* dativa.tools.SQLClient - a wrapper for any PEP249 compliant database client with logging and splitting of queries
* dativa.tools.pandas.CSVHandler - improved CSV handling for Pandas
* dativa.tools.pandas.ParquetHandler - improved Parquet handling for pandas
* dativa.tools.pandas.Shapley - Shapley attribution modelling using pandas DataFrames

There are also some useful support functions for Pandas date and time handling.
As well as a function to save data out in a format suitable for Athena.

## Installation

```
pip install dativatools
```

Note that Dativa Tools uses loose binding to required libraries and the required binaries are thus not automatically installed with the package and you can import classes and functions from dativa tools without the required libraries installed. An ImportError is only raised at runtime if you are looking to use a function that depends on another package that is not installed. 

The required libraries are listed in requirements.txt and include:
* pyarror for ParquetHandler 
* pandas for all of the pandas extensions
* awsretry and boto3 for any functions requiring AWS access
* s3fs for many functions using S3
* blist for Shapley
* pycryptodome for encrypting CSVs in CSVHandler
* chardet for sniffing encodings in CSVHandler
* requests for PipelineClient

## Description

### dativa.tools.aws.AthenaClient
 An easy to use client for AWS Athena that will create tables from S3 buckets (using AWS Glue) and run queries against these tables. It support full customisation of SerDe and column names on table creation.

 Examples:

#### Creating tables

The library creates a temporary Glue crawler which is deleted after use, and will also create the database if it does not exist.

```python
from dativa.tools.aws import AthenaClient
ac = AthenaClient("us-east-1", "my_athena_db")
ac.create_table(table_name='my_first_table',
                crawler_target={'S3Targets': [
                    {'Path': 's3://my-bucket/table-data'}]}
                )

# Create a table with a custom SerDe and column names, typical for CSV files
ac.create_table(table_name='comcast_visio_match',
                crawler_target={'S3Targets': [
                    {'Path': 's3://my-bucket/table-data-2', 'Exclusions': ['**._manifest']}]},
                serde='org.apache.hadoop.hive.serde2.OpenCSVSerde',
                columns=[{'Name': 'id', 'Type': 'string'}, {
                    'Name': 'device_id', 'Type': 'string'}, {'Name': 'subscriber_id', 'Type': 'string'}]
                )
```

#### Running queries

```python
from dativa.tools.aws import AthenaClient

ac = AthenaClient("us-east-1", "my_athena_db")
ac.add_query(sql="select * from table",
                 name="My first query",
                 output_location= "s3://my-bucket/query-location/")

ac.wait_for_completion()
```

#### Fetch results of query
```python
from dativa.tools.aws import AthenaClient

ac = AthenaClient("us-east-1", "my_athena_db")
query = ac.add_query(sql="select * from table",
                     name="My first query",
                     output_location= "s3://my-bucket/query-location/")

ac.wait_for_completion()
ac.get_query_result(query)
```



#### Running queries with the output in Parquet and create an Athena table

```python
from dativa.tools.aws import AthenaClient, S3Csv2Parquet

scp = S3Csv2Parquet(region="us-east-1",
                    template_location="s3://my-bucket/glue-template-path/")
ac = AthenaClient("us-east-1", "my_athena_db", s3_parquet=scp)
ac.add_query(sql="select * from table",
                 name="my query that outputs Parquet",
                 output_location="s3://my-bucket/query-location/",
                 parquet=True)

ac.wait_for_completion()

ac.create_table({'S3Targets': [{'Path': "s3://my-bucket/query-location/"}]},
                                        table_name="query_location")
```


### dativa.tools.aws.S3Client

 An easy to use client for AWS S3 that adds some functionality
 Examples:

#### S3Location
Class that parses out an S3 location from a passed string. Subclass of `str`
so supports most string operations.

Also contains properties .bucket, .key, .path, .prefix and method .join()

* param s3_str: string representation of s3 location, accepts most common formats
    ```
    eg:
        - 's3://bucket/folder/file.txt'
        - 'bucket/folder'
        - 'http[s]://s3*.amazonaws.com/bucket-name/'
    also accepts None if using `bucket` and `key` keyword
    ```
* param bucket: ignored if s3_str is not None. can specify only bucket for
    bucket='mybucket' - 's3://mybucket/' or in conjuction with `key`
* param key: ignored if s3_str is not None. Bucket must be set.
    bucket='mybucket', key='path/to/file' - 's3://mybucket/path/to/file'
* param ignore_double_slash: default False. If true allows s3 locations containing '//'
    these are valid s3 paths, but typically result from mistaken joins



#### Batch deleting of files on S3

```python
from dativa.tools.aws import S3Client

# Delete all files in a folder
s3 = S3Client()
s3.delete_files(bucket="bucket_name", prefix="/delete-this-folder/")

# Delete only .csv.metadata files in a folder
s3 = S3Client()
s3.delete_files(bucket="bucket_name", prefix="/delete-this-folder/", suffix=".csv.metadata")

```

#### Copy files from folder in local filesystem to s3 bucket

```python
from dativa.tools.aws import S3Client

s3 = S3Client()
s3.put_folder(source="/home/user/my_folder", bucket="bucket_name", destination="backup/files")

# Copy all csv files from folder to s3
s3.put_folder(source="/home/user/my_folder", bucket="bucket_name", destination="backup/files", file_format="*.csv")
```

### dativa.tools.SQLClient

A SQL client that wraps any PEP249 compliant connection object and provides detailed logging and simple query execution.

It takes the following parameters when instantaited:
- db_connection - a PEP257 compatible database connection
- logger - the logger to use
- logging_level - the level at which to log most output
- log_query_text - whether to log all of the query text
- humour - if set to true output jokes to pass the time of day waiting for queries to complete

#### execute_query
Runs a query and ignores any output

Parameters:

- query - the query to run, either a SQL file or a SQL query
- parameters - a dict of parameters to substitute in the query
- replace - a dict or items to be replaced in the SQL text
- first_to_run - the index of the first query in a mult-command query to be executed

#### execute_query_to_df

Runs a query and returns the output of the final statement in a DataFrame.

Parameters:

- query - the query to run, either a SQL file or a SQL query
- parameters - a dict of parameters to substitute in the query
- replace - a dict or items to be replaced in the SQL text
- first_to_run - the index of the first query in a mult-command query to be executed


#### def execute_query_to_csv

Runs a query and writes the output of the final statement to a CSV file.

Parameters:

- query - the query to run, either a SQL file or a SQL query
- csvfile - the file name to save the query results to
- parameters - a dict of parameters to substitute in the query
- replace - a dict or items to be replaced in the SQL text

#### Example code

```python
import os
import psycopg2
from dativa.tools import SqlClient

# set up the SQL client from environment variables
sql = SqlClient(psycopg2.connect(
    database=os.environ["DB_NAME"],
    user=os.environ["USER"],
    password=os.environ["PASSWORD"],
    host=os.environ["HOST"],
    port=os.environ["PORT"],
    client_encoding="UTF-8",
    connect_timeout=10))

# create the full schedule table
df = sql.execute_query_to_df(query="sql/my_query.sql",
                             parameters={"start_date": "2018-01-01",
                                         "end_date": "2018-02-01"})
```

### dativa.tools.log_to_stdout

A convenience function to redirect a specific logger and its children to stdout

```python
import logging
from dativa.tools import log_to_stdout

log_to_stdout("dativa.tools", logging.DEBUG)
```

### dativa.tools.pandas.CSVHandler

A wrapper for pandas CSV handling to read and write dataframes
that is provided in pandas with consistent CSV parameters and
sniffing the CSV parameters automatically.
Includes reading a CSV into a dataframe, and writing it out to a string.

#### Parameters

- base_path: the base path for any CSV file read, if passed as a string
- detect_parameters: whether the encoding of the CSV file should be automatically detected
- encoding: the encoding of the CSV files, defaults to UTF-8
- delimiter: the delimeter used in the CSV, defaults to ,
- header: the index of the header row, or -1 if there is no header
- skiprows: the number of rows at the beginning of file to skip
- quotechar: the quoting character to use, defaults to ""
- include_index: specifies whether the index should be written out, default to False
- compression: specifies whether the data should be compressed, default to 'infer', current support for writing out gzip and zip compressed files
- nan_values: an array of possible NaN values, the first of which is used when writign out, defaults to None
- line_terminator: the line terminator to be used
- quoting: the level of quoting, defaults to QUOTE_MINIMAL
- decimal: the decimal character, defaults to '.'
- chunksize: if specified the CSV is written out in chunks
- aes_key: bytes, allowable lengths are 16, 24, 32 
- zipfile_compression: the type of zip compressions to use, default to ZIP_DEFLATED
 
for decrypting and encrypting CSVs when passing to a dataframe, this uses AES CFB encryption via Pycryptodome
- aes_iv: bytes, must have length of 16

the initialization vector for the AES CFB encryption via Pycryptodome. If aes_key is specified and this is 
not, it will auto-generate an iv and prefix it to the encrypted bytes. 

#### load_df

Opens a CSV file using the specified configuration for the class and raises an exception if the encoding is unparseable.
Detects if base_path is an S3 location and loads data from there if required.

Parameters:

- file - File path. Should begin with 's3://' to load from S3 location.
- force_dtype - Force data type for data or columns, defaults to None
- kwargs - any of the keyword arguments used to create the class can also be passed to load_df

Returns:

- dataframe

#### save_df

Writes a formatted string from a dataframe using the specified configuration for the class the file. Detects if base_path is an S3 location and saves data there if required.

Parameters:

- df - Dataframe to save
- file - File path. Should begin with 's3://' to save to an S3 location.
- kwargs - any of the keyword arguments used to create the class can also be passed to save_df

#### df_to_string

Returns a formatted string from a dataframe using the specified configuration for the class.

Parameters:

- df - Dataframe to convert to string
- kwargs - any of the keyword arguments used to create the class can also be passed to df_to_string

Returns:

- string
 
#### Example code

```python
from dativa.tools.pandas import CSVHandler

# Create the CSV handler
csv = CSVHandler(base_path='s3://my-bucket-name/')

# Load a file
df = csv.load_df('my-file-name.csv')

# Create a string
str_df = csv.df_to_string(df)

# Save a file
csv.save_df(df, 'another-path/another-file-name.csv')
```

### Support functions for Pandas

* dativa.tools.pandas.is_numeric - a function to check whether a series or string is numeric
* dativa.tools.pandas.string_to_datetime - a function to convert a string, or series of strings to a datetime, with a strptime date format that supports nanoseconds
* dativa.tools.pandas.datetime_to_string - a function to convert a datetime, or a series of datetimes to a string, with a strptime date format that supports nanoseconds
* dativa.tools.pandas.format_string_is_valid - a function to confirm whether a strptime format string returns a date
* dativa.tools.pandas.get_column_name - a function to return the name of a column from a passed column name or index.
* dativa.tools.pandas.get_unique_column_name - a function to return a unique column name when adding new columns to a DataFrame

### dativa.tools.pandas.ParquetHandler

ParquetHandler class, specify path of parquet file,
and get pandas dataframe for analysis and modification.

* param base_path                       : The base location where the parquet_files are stored.
* type base_path                        : str
* param row_group_size                  : The size of the row groups while writing out the parquet file.
* type row_group_size                   : int
* param use_dictionary                  : Specify whether to use boolean encoding or not
* type use_dictionary                   : bool
* param use_deprecated_int96_timestamps : Write nanosecond resolution timestamps to INT96 Parquet format.
* type use_deprecated_int96_timestamps  : bool
* param coerce_timestamps               : Cast timestamps a particular resolution. Valid values: {None, 'ms', 'us'}
* type coerce_timestamps                : str
* param compression                     : Specify the compression codec.
* type compression                      : str

```python
from dativa.tools.pandas import CSVHandler, ParquetHandler

# Read a parquet file
pq_obj = ParquetHandler()
df_parquet = pq_obj.load_df('data.parquet')

# save a csv_file to parquet
csv = CSVHandler(csv_delimiter=",")
df = csv.load_df('emails.csv')
pq_obj = ParquetHandler()
pq_obj.save_df(df, 'emails.parquet')
```
#### save_df
Saves the df as parquet to the file path given to it, similar to CSVHandler save_df.

##### Parameters

* param df                              : A pandas dataframe to write to original file location of parquet file.
* type df                               : pandas.DataFrame
* param row_group_size                  : The size of the row groups while writing out the parquet file.
* type row_group_size                   : int
* param use_deprecated_int96_timestamps : Write nanosecond resolution timestamps to INT96 Parquet format.
* type use_deprecated_int96_timestamps  : bool
* param coerce_timestamps               : Cast timestamps a particular resolution. Valid values: {None, 'ms', 'us'}
* type coerce_timestamps                : str
* param compression                     : Specify the compression codec.
* type compression                      : str
* param schema                          : Used to set the desired schema for pyarrow table, if not provided schema is inferred
* type schema                           : pyarrow.lib.Schema or dict
* param infer_other_dtypes              : Used when schema is specified. When True, if there are columns not specified in schema then their dtypes are inferred. When false, if there are columns not specified in schema then raise an error. Default behaviour is False.
* type infer_other_dtypes               : bool

For convenience, ParquetHandler allows a python dict to be passed to the schema argument. The dict should have column names as the keys and desired types as the values. A dict or schema for only some of the columns may be passed, the types for the rest of the columns will then be inferred. The types are inferred by looking at the types for the non-null values in each column. An error is raised if there multiple types in each column.

Example code of how to pass a dict to the schema argument. In this example, only columns `col1` and `col2` are given types, any other columns will have their types inferred.

```python
pq_obj = ParquetHandler()

dict_schema = {'col1': str, 'col3': int}
pq_obj.save_df(test_df, new_file_path, schema=dict_schema)
```

Example code on how to generate pyarrow.lib.schema objects and how to pass the schema to save_df.

```python
pq_obj = ParquetHandler()

fields = [
    pa.field("col1", pa.int64()),
    pa.field("col2", pa.string())]
my_schema = pa.schema(fields)
pq_obj.save_df(test_df, new_file_path, schema=my_schema)
```

### dativa.tools.pandas athena_partition

A function to handle partitioning and saving a pandas DataFrame in a format compatible with athena. Using one or more specified column from the DataFrame being saved.

##### Parameters

* param df                      : The data frame to be partitioned
* type df                       : pandas.DataFrame
* param partition_categories    : The columns to partition the data on
* type partition_categories     : list
* param file_handler            : The appropriate file handler to save the data, currently tested for dativa CSVHandler and ParquetHandler support, other handlers are untested
* type file_handler             : obj
* param suffix                  : The extension the file should be saved with, .csv for csv, and .parquet for parquet
* type suffix                   : str
* param columns_to_keep         : Columns to keep from the data frame, if not supplied default behaviour is to keep all columns
* type columns_to_keep          : list
* param date_time_format        : To minimise chances of overwrite the saved files contain the date time of when this function was called, this param specifies the format of the date time in strftime format
* type date_time_format         : str
* param name                    : If provided all files filename will start with this
* type name                     : str
* param partition_string        : Allows formatting folder names, will be dependant on how many partition categories there are, defaults to creating folders and sub folders in order of partitioning
* type partition_string         : str
* param partition_dtypes        : Can pass argument to set the dtype of a particular column, to ensure proper grouping, also doubles to checking the column doesnt contain values of an unexpected dtype
* type partition_dtypes         : list
* param kwargs                  : Any additional key word arguments to be passed to the handler                  
* return                        : Returns a full list of all file paths created, doesnt return base path as part of this



### dativa.tools.aws import S3Csv2Parquet
 An easy to use module for converting csv files on s3 to praquet using aws glue jobs.
 For S3 access and glue access suitable credentials should be available in '~/.aws/credentials' or the AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY environment variables.

#### S3Csv2Parquet
Parameters:

- region - str,
           AWS region in which glue job is to be run
- template_location - str,
                      S3 bucket Folder in which template scripts are
                      located or need to be copied.
                      format s3://bucketname/folder/
                      it is not clear to those unfamiliar with glue what this is.
- glue_role - str,
              Name of the glue role which need to be assigned to the
              Glue Job.
- max_jobs - int, default 5
             Maximum number of jobs the can run concurrently in the queue
- retry_limit - int, default 3
                Maximum number of retries allowed per job on failure

#### convert
Parameters:

- csv_path - str or list of str for multiple files,
             s3 location of the csv file
             format s3://bucketname/folder/file.csv
             Pass a list for multiple files
- output_folder - str, default set to folder where csv files are located 
                  s3 location at which paraquet file should be copied
                  format s3://bucketname/folder
- schema - list of tuples,
           If not specified schema is inferred from the file
           format [(column1, datatype), (column2, datatype)]
           Supported datatypes are boolean, double, float, integer,
           long, null, short, string
- name - str, default 'parquet_csv_convert'
         Name to be assigned to glue job
- allocated_capacity - int, default 2
                       The number of AWS Glue data processing units (DPUs) to allocate to this Job.
                       From 2 to 100 DPUs can be allocated
- delete_csv - boolean, default False
               If set source csv files are deleted post successful completion of job
- separator - character, default ','
              Delimiter character in csv files
- with_header- int, default 1
              Specifies whether to treat the first line as a header
              Can take values 0 or 1
- compression - str, default None
                If not specified compression is not applied.
                Can take values snappy, gzip, and lzo
- partition_by - list of str, default None
                 List containing columns to partition data by
- mode - str, default append
         Options include:
         overwrite: will remove data from output_folder before writing out
                    converted file.
         append: Will write out to  output_folder without deleting existing
                 data.
         ignore: Silently ignore this operation if data already exists.

#### Example

```python
from dativa.tools.aws import S3Csv2Parquet

# Initial setup
csv2parquet_obj = S3Csv2Parquet("us-east-1", "s3://my-bucket/templatefolder")

# Create/update a glue job to convert csv files and execute it
csv2parquet_obj.convert("s3://my-bucket/file_to_be_converted_1.csv")
csv2parquet_obj.convert("s3://my-bucket/file_to_be_converted_2.csv")

# Wait for completion of jobs 
csv2parquet_obj.wait_for_completion()
```

### dativa.tools.pandas.Shapley

Shapley attribution of scores to members of sets.

See [medium](https://towardsdatascience.com/one-feature-attribution-method-to-supposedly-rule-them-all-shapley-values-f3e04534983d)
or [wiki](https://en.wikipedia.org/wiki/Shapley_value) for details on the math. The aim is to apportion scores between the members of a set
responsible for producing that score.

Takes two DataFrames as input, one containing impressions from campaigns and the other containing conversions.

eg. campaigns

|viewer_id|campaign_id|
| :----:|:-----:|
|20|B|
|19|B|
|12|B|
|6|A|
|17|B|
|12|B|
|8|B|
|3|A|
|18|A|

where a campaign_id might be a campaign that an individual has interacted with. Each viewer / campaign
pair is only considered once.

eg 2. conversions

|viewer_id|
|: --- :|
|14|
|12|
|2|
|3|
|11|

these are individuals that have converted. From this a conversion rate is calculated which is used as a score.
That score is apportioned among the campaigns.

Typically not all combinations of impressions are present (particularly in where there are lots of 
campaigns being run). The missing combinations are assigned a default score, which might be an average conversion rate 
or similar. This is passed to the class constructor as `default_score` and must be numeric.

### Example code

```python

s = Shapley(df_campaigns, df_conversions, 'viewer_id', 'campaign_id', default_score=0.01)

results = s.run()

```

## dativa.tools.FileValidation
A module to validate the files present in a given directory based on glob pattern matching. The 
FileValidation class initialises and checks a set of rules for a file validation, this can then be run for various 
paths and glob pattern matches via a method (run_validator). Validation is be based on 
various properties - time last modified, size and the number of files which match criteria. Examples on how to use 
the file validation are provided below.

FileValidation Arguments:

* timestamp: (tuple or str or None) strings for min and max time (str or None, str or None) in UTC. This is
 read in with datetime.strptime, so must use compatible formats 
* file_size: (tuple or int or None) min and max size in bytes (int or None, int or None), treats single int
 as minimum 
* file_count: (tuple or int or None) min and max file count, treats single int as minimum
* timestamp_format: (str) string for a valid timestamp, specified format for both max and min timestamp,
      uses datetime.strptime, hence must be in compatible format. 

run_validator Arguments:

* path: (str) path to the files - can either be a path for S3Location or an absolute local file path.  CANNOT HAVE '/' AS THE FINAL CHARACTER.
* glob_pattern: (str) pattern of glob files to be examined.  CANNOT HAVE '/' AS THE FIRST CHARACTER.
* consider_correctly_formed_files: (bool) if False, consider malformed files (which do not match validation) for the 
file_count argument of FileValidation
* raise_exceptions: (bool) whether to raise exception when finding files which do not match validation criteria

### Example codes 

The code can either return a list of files (either all which match the criteria or those which do not) or raise an 
exception if any files fail the validation.  This can be applied to either files on S3 or on the local filesystem.

The files to be validated are specified via s3fs.glob for S3 (see https://s3fs.readthedocs.io/en/latest/) and glob.glob 
for local files (see https://docs.python.org/3/library/glob.html).

### Check number of CSVs in a given path
```python
from dativa.tools import FileValidation
# ensure there are between 10 and 100 CSVs in your target folder
# this command ignores other file extensions (e.g. .tsv files) as they aren't picked up by the glob pattern          
fv = FileValidation(file_count=(10, 100))   # between 10 and 100 bytes 
# if validation is not met, raise an exception
fv.run_validator(path="s3://some-bucket/some-path",
                 glob_pattern="*.csv",
                 raise_exceptions=True)
```

### Check that a specific file was last modified on a specific date and is smaller than a given size 
```python
from dativa.tools import FileValidation

fv = FileValidation(file_size=(None, 2*2**10),  # 2 KB
                    timestamp=("2018-12-25", "2018-12-25"), # made on 25th Dec 2018 
                    timestamp_format="%Y-%m-%d")
# if validation is not met, raise an exception                    
fv.run_validator(path="s3://some-bucket/some-path",
                 glob_pattern="some-specific-key.csv",
                 raise_exceptions=True)
```

### Return file which do not match a certain size and age range
```python
from dativa.tools import FileValidation
from datetime import datetime
fv = FileValidation(file_size=(10, None), # minimum file size of 10 bytes 
                    # no minimum time, earliest files made today
                    timestamp=(None, datetime.utcnow().strftime("%Y-%m-%d")),
                    timestamp_format="%Y-%m-%d")
                    
# return files in dictionary                    
list_of_bad_files = fv.run_validator(path="/Users/your-name/absolute/file/path",
                                     glob_pattern="*",
                                     consider_correctly_formed_files=False)
```

### Local file paths must be _absolute_ paths rather than relative paths
```python
from dativa.tools import FileValidation
fv = FileValidation(file_size=(10, 10*2**20) # between 10 bytes and 10 GB
                    )
# return files which do not match the specified validation                    
list_of_bad_files = fv.run_validator(path="/Users/your-name/absolute/file/path",
                                     glob_pattern="*",
                                     consider_correctly_formed_files=False)

# return files which match the specified validation                    
list_of_good_files = fv.run_validator(path="/Users/your-name/absolute/file/path",
                                      glob_pattern="*",
                                      consider_correctly_formed_files=True)
```

### NOTE - both the path must not end with a '/' AND glob_pattern must not start with one
```python
from dativa.tools import FileValidation
fv = FileValidation(file_size=(10, None), # minimum file size of 10 bytes 
                    )
                    
# return files in dictionary                    
this_will_not_run = fv.run_validator(path="/Users/your-name/absolute/file/path/",
                                     glob_pattern="/*",
                                     consider_correctly_formed_files=False)
also_will_not_run = fv.run_validator(path="/Users/your-name/absolute/file/path/",
                                     glob_pattern="*",
                                     consider_correctly_formed_files=False)
again_will_not_run = fv.run_validator(path="/Users/your-name/absolute/file/path",
                                      glob_pattern="/*",
                                      consider_correctly_formed_files=False)
``` 

## Legacy classes

The modules in the dativatools namespace are legacy only and will be deprecated in future.