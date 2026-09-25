# PySpark Practice --- Individual SparkSession

A structured PySpark practice repository covering fundamental DataFrame
transformations, joins, and aggregations. Each Python file is designed
as an independent practice exercise and can be executed separately with
its own `SparkSession`.

## Project Overview

This repository is created to strengthen practical knowledge of PySpark
and distributed data processing concepts through small, focused scripts.

The current modules cover:

-   Basic DataFrame transformations
-   Join operations
-   Grouping and aggregation functions
-   CSV-based input data

## Project Structure

``` text
pyspark_practice/
│
├── src/
│   ├── 00_reading_practice/
│   │   ├── 01_read_csv.py
│   │   ├── 02_read_json.py
│   │   ├── 03_read_parquet.py
│   │   └── 04_read_delta.py
│   │
│   ├── 01_basic_transformations/
│   │   ├── 01_select.py
│   │   ├── 02_filter.py
│   │   ├── 03_where.py
│   │   ├── 04_withColumn.py
│   │   ├── 05_when_otherwise.py
│   │   ├── 06_column_expressions.py
│   │   └── 07_aliases.py
│   │
│   ├── 02_joins/
│   │   ├── 01_inner_join.py
│   │   ├── 02_left_join.py
│   │   ├── 03_full_outer_join.py
│   │   ├── 04_semi_join.py
│   │   ├── 05_anti_join.py
│   │   ├── 06_join_conditions.py
│   │   ├── 07_duplicate_columns.py
│   │   └── 08_null_values_in_joins.py
│   │
│   └── 03_aggregations/
│       ├── 01_groupBy.py
│       ├── 02_agg.py
│       ├── 03_sum.py
│       ├── 04_count.py
│       ├── 05_avg.py
│       ├── 06_min_max.py
│       ├── 07_multiple_aggregations.py
│       └── 08_multiple_grouping_columns.py
│
├── data/
│   ├── customers.csv
│   ├── departments.csv
│   ├── employees.csv
│   └── orders.csv
│
└── README.md
```

## Topics Covered

### 1. Reading Data

This module demonstrates how to read data from different file formats using PySpark's `DataFrameReader`.

| File | Concept |
|---|---|
| `01_read_csv.py` | Read CSV files into a PySpark DataFrame |
| `02_read_json.py` | Read JSON files into a PySpark DataFrame |
| `03_read_parquet.py` | Read Parquet files into a PySpark DataFrame |
| `04_read_delta.py` | Read Delta Lake tables or Delta-formatted data |

Common reading operations include:

- `spark.read`
- `DataFrameReader`
- Schema inference
- Explicit schemas
- Header handling for CSV files
- Reading structured and columnar data formats

### 2. Basic Transformations

This module focuses on selecting, filtering, modifying, and renaming
DataFrame columns.

  File                         Concept
  ---------------------------- ----------------------------------------------
  `01_select.py`               Select specific columns from a DataFrame
  `02_filter.py`               Filter rows using conditions
  `03_where.py`                Filter rows using the `where()` method
  `04_withColumn.py`           Create or replace a DataFrame column
  `05_when_otherwise.py`       Apply conditional logic to columns
  `06_column_expressions.py`   Work with PySpark column expressions
  `07_aliases.py`              Rename columns and expressions using aliases

### 3. Joins

This module demonstrates how to combine data from multiple DataFrames.

  -----------------------------------------------------------------------
  File                                Concept
  ----------------------------------- -----------------------------------
  `01_inner_join.py`                  Return matching records from both
                                      DataFrames

  `02_left_join.py`                   Preserve all records from the left
                                      DataFrame

  `03_full_outer_join.py`             Preserve records from both
                                      DataFrames

  `04_semi_join.py`                   Return left-side records with a
                                      match in the right DataFrame

  `05_anti_join.py`                   Return left-side records without a
                                      match in the right DataFrame

  `06_join_conditions.py`             Define and apply join conditions

  `07_duplicate_columns.py`           Handle duplicate column names after
                                      joins

  `08_null_values_in_joins.py`        Understand and handle null values
                                      in join operations
  -----------------------------------------------------------------------

### 4. Aggregations

This module covers summarizing and grouping data using PySpark
aggregation functions.

  -----------------------------------------------------------------------
  File                                Concept
  ----------------------------------- -----------------------------------
  `01_groupBy.py`                     Group records based on one or more
                                      columns

  `02_agg.py`                         Apply one or more aggregation
                                      expressions

  `03_sum.py`                         Calculate the sum of values

  `04_count.py`                       Count records or non-null values

  `05_avg.py`                         Calculate average values

  `06_min_max.py`                     Find minimum and maximum values

  `07_multiple_aggregations.py`       Apply multiple aggregation
                                      functions together

  `08_multiple_grouping_columns.py`   Group data using multiple columns
  -----------------------------------------------------------------------

## Dataset Description

The `data` directory contains CSV files used for practicing joins and
aggregations.

  File                Purpose
  ------------------- --------------------------------
  `customers.csv`     Customer-related information
  `departments.csv`   Department-related information
  `employees.csv`     Employee-related information
  `orders.csv`        Order-related information

The exact columns and relationships depend on the dataset definitions
used in each exercise.

## Requirements

Install the required software before executing the scripts:

-   Python 3.x
-   Java-compatible environment required by Apache Spark
-   PySpark
-   Git
-   VS Code or another Python-compatible IDE

Install PySpark using pip:

``` bash
pip install pyspark
```

Verify the installation:

``` bash
python -c "import pyspark; print(pyspark.__version__)"
```



