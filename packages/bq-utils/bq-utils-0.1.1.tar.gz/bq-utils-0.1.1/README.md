# bq-utils - A collection of BigQuery utilities
Currently the utilities covered in this library are limited to managing table and view descriptions.
It's quite useful to have the field descriptions available on 
the schema tab and on the query editor pane on the BigQuery UI and this library helps you with uploading them and copying them around.
## Install
```bash
pip install bq-utils
```
## Python
### Copy descriptions between tables and views
```python
from google.cloud import bigquery
from bqutils.bigquery_description_manager import BigQueryDescriptionManager

bq_client = bigquery.Client()
description_manager = BigQueryDescriptionManager(bq_client)
source_table_id = 's_project.s_dataset.s_table'
target_table_id = 't_project.t_dataset.t_table'
description_manager.copy_field_descriptions(source_table_id, target_table_id)
```

### Upload descriptions from csv
```python
from google.cloud import bigquery
from bqutils.bigquery_description_manager import BigQueryDescriptionManager

bq_client = bigquery.Client()
description_manager = BigQueryDescriptionManager(bq_client)
descriptions_csv_path = 'table_descriptions.csv'
target_table_id = 't_project.t_dataset.t_table'
description_manager.upload_field_descriptions(descriptions_csv_path, target_table_id)
```

## Command line
### Usage
```bash
usage: __main__.py [-h] [--source SOURCE] --target TARGET
                   [--csv_path CSV_PATH] [--debug]
                   {desccopy,descupload}

Copy or upload field descriptions for BigQuery tables/views

positional arguments:
  {desccopy,descupload}

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       fully-qualified source table ID
  --target TARGET       fully-qualified target table ID
  --csv_path CSV_PATH   path for the csv file
  --debug               set debug mode on, default is false
```
### Copy descriptions between tables and views
```bash
python -m bqutils desccopy --source s_project.s_dataset.s_table --target t_project.t_dataset.t_table
```

### Upload descriptions from csv
```bash
python -m bqutils descupload --csv_path table_descriptions.csv --target t_project.t_dataset.t_table
```