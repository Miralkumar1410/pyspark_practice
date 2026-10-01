# PySpark Practice 

## Project Overview


The current modules cover:

-   Basic DataFrame transformations
-   Join operations
-   Grouping and aggregation functions
-   Advanced PySpark functions
-   Window functions
-   Nested data processing
-   User Defined Functions (UDFs)
-   Slowly Changing Dimensions (SCD)
-   PySpark basic syntax
-   Built-in PySpark functions
-   Pandas `applyInPandas()`
-   Partition management
-   Data skew and salting
-   Reading and writing multiple data formats
-   CSV and JSON-based input data

## Project Structure

```text
pyspark_practice/
│
├── src/
│   ├── reading_practice/
│   │   ├── 01_read_csv.py
│   │   ├── 02_read_json.py
│   │   ├── 03_read_parquet.py
│   │   └── 04_read_delta.py
│
│   ├── writing_practice/
│   │   ├── 01_write_csv.py
│   │   ├── 02_write_json.py
│   │   ├── 03_write_parquet.py
│   │   └── 04_write_delta.py
│
│   ├── basic_transformations/
│   │   ├── 01_select.py
│   │   ├── 02_filter.py
│   │   ├── 03_where.py
│   │   ├── 04_withColumn.py
│   │   ├── 05_when_otherwise.py
│   │   ├── 06_column_expressions.py
│   │   └── 07_aliases.py
│
│   ├── joins/
│   │   ├── 01_inner_join.py
│   │   ├── 02_left_join.py
│   │   ├── 03_full_outer_join.py
│   │   ├── 04_semi_join.py
│   │   ├── 05_anti_join.py
│   │   ├── 06_join_conditions.py
│   │   ├── 07_duplicate_columns.py
│   │   └── 08_null_values_in_joins.py
│
│   ├── aggregations/
│   │   ├── 01_groupBy.py
│   │   ├── 02_agg.py
│   │   ├── 03_sum.py
│   │   ├── 04_count.py
│   │   ├── 05_avg.py
│   │   ├── 06_min_max.py
│   │   ├── 07_multiple_aggregations.py
│   │   └── 08_multiple_grouping_columns.py
│
│   ├── advanced_functions/
│   │   ├── 01_string_functions.py
│   │   ├── 02_numeric_functions.py
│   │   ├── 03_date_time_functions.py
│   │   ├── 04_aggregation_functions.py
│   │   ├── 05_joins.py
│   │   └── 06_array_functions.py
│
│   ├── window_functions/
│   │   ├── 01_row_number.py
│   │   ├── 02_rank.py
│   │   ├── 03_dense_rank.py
│   │   ├── 04_lag.py
│   │   ├── 05_lead.py
│   │   ├── 06_running_totals.py
│   │   ├── 07_Window_partitionBy.py
│   │   └── 08_Window_orderBy.py
│
│   ├── nested_data/
│   │   ├── 01_arrays.py
│   │   ├── 02_structs.py
│   │   ├── 03_explode.py
│   │   ├── 04_from_json.py
│   │   ├── 05_nested_json_parsing.py
│   │   └── 06_accessing_nested_fields.py
│
│   ├── udf/
│   │   ├── 01_python_udf.py
│   │   ├── 02_udf_with_multiple_columns.py
│   │   ├── 03_udf_condition.py
│   │   └── 04_udf_vs_builtin.py
│
│   ├── scd/
│   │   ├── 01_type_1.py
│   │   ├── 02_type_2.py
│   │   └── 03_type_3.py
│
│   ├── pyspark_basic_syntax/
│   │   └── 01_pyspark_basic_syntax.py
│
│   ├── built_in_functions/
│   │   ├── 01_limit_function.py
│   │   ├── 02_where_function.py
│   │   ├── 03_like_function.py
│   │   ├── 04_withColumnRenamed_function.py
│   │   ├── 05_drop_function.py
│   │   ├── 06_distinct_function.py
│   │   ├── 07_dropDuplicates_function.py
│   │   ├── 08_sort_function.py
│   │   ├── 09_fillna_function.py
│   │   ├── 10_dropna_function.py
│   │   ├── 11_union_function.py
│   │   ├── 12_unionAll_function.py
│   │   └── 13_pivot_function.py
│
│   ├── applyinpandas/
│   │   └── 01_applyinpandas_function.py
│
│   ├── partitions/
│   │   ├── 01_check_no_of_partitions.py
│   │   ├── 02_repartition.py
│   │   └── 03_coalesce.py
│
│   └── data_skew/
│       └── 01_salting.py
│
├── data/
│   ├── customers.csv
│   ├── departments.csv
│   ├── employees.csv
│   ├── orders.csv
│   └── customers.json
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

### 5. Advanced Functions

This module covers commonly used PySpark functions for practical DataFrame operations.

| File | Concept |
|---|---|
| `01_string_functions.py` | String manipulation and transformation functions |
| `02_numeric_functions.py` | Numeric and mathematical functions |
| `03_date_time_functions.py` | Date and time functions |
| `04_aggregation_functions.py` | Aggregation functions |
| `05_joins.py` | Join operations |
| `06_array_functions.py` | Array functions |

### 6. Window Functions

This module covers analytical operations using PySpark window specifications.

| File | Concept |
|---|---|
| `01_row_number.py` | `row_number()` |
| `02_rank.py` | `rank()` |
| `03_dense_rank.py` | `dense_rank()` |
| `04_lag.py` | `lag()` |
| `05_lead.py` | `lead()` |
| `06_running_totals.py` | Running totals |
| `07_Window_partitionBy.py` | `Window.partitionBy()` |
| `08_Window_orderBy.py` | `Window.orderBy()` |

### Window Function Concepts

- `row_number()`
- `rank()`
- `dense_rank()`
- `lag()`
- `lead()`
- Running totals
- `Window.partitionBy()`
- `Window.orderBy()`

### 7. Nested Data

This module covers working with arrays, structs, JSON data, and nested fields in PySpark.

| File | Concept |
|---|---|
| `01_arrays.py` | Arrays in PySpark |
| `02_structs.py` | Structs in PySpark |
| `03_explode.py` | `explode()` for nested collections |
| `04_from_json.py` | Parse JSON strings using `from_json()` |
| `05_nested_json_parsing.py` | Nested JSON parsing |
| `06_accessing_nested_fields.py` | Access nested fields |

### 8. User Defined Functions

This module covers Python UDFs, UDFs with multiple columns, conditional UDFs, and comparison with built-in Spark functions.

| File | Concept |
|---|---|
| `01_python_udf.py` | Python UDF |
| `02_udf_with_multiple_columns.py` | UDF with multiple columns |
| `03_udf_condition.py` | Conditional UDF |
| `04_udf_vs_builtin.py` | UDF versus built-in functions |

### 9. Slowly Changing Dimensions

This module covers different Slowly Changing Dimension strategies.

| File | Concept |
|---|---|
| `01_type_1.py` | SCD Type 1 |
| `02_type_2.py` | SCD Type 2 |
| `03_type_3.py` | SCD Type 3 |

### 10. Writing Data

This module demonstrates writing DataFrames to different file formats.

| File | Concept |
|---|---|
| `01_write_csv.py` | Write DataFrame data to CSV |
| `02_write_json.py` | Write DataFrame data to JSON |
| `03_write_parquet.py` | Write DataFrame data to Parquet |
| `04_write_delta.py` | Write DataFrame data to Delta |

### 11. PySpark Basic Syntax

This module contains basic PySpark syntax practice.

| File | Concept |
|---|---|
| `01_pyspark_basic_syntax.py` | PySpark basic syntax |

### 12. Built-in Functions

This module contains practice with commonly used PySpark DataFrame functions.

| File | Concept |
|---|---|
| `01_limit_function.py` | `limit()` |
| `02_where_function.py` | `where()` |
| `03_like_function.py` | `like()` |
| `04_withColumnRenamed_function.py` | `withColumnRenamed()` |
| `05_drop_function.py` | `drop()` |
| `06_distinct_function.py` | `distinct()` |
| `07_dropDuplicates_function.py` | `dropDuplicates()` |
| `08_sort_function.py` | `sort()` |
| `09_fillna_function.py` | `fillna()` |
| `10_dropna_function.py` | `dropna()` |
| `11_union_function.py` | `union()` |
| `12_unionAll_function.py` | `unionAll()` |
| `13_pivot_function.py` | `pivot()` |

### 13. Pandas `applyInPandas()`

This module contains practice with applying pandas functions to PySpark grouped data using `applyInPandas()`.

| File | Concept |
|---|---|
| `01_applyinpandas_function.py` | `applyInPandas()` |

### 14. Partitions

This module covers inspecting and managing Spark DataFrame partitions.

| File | Concept |
|---|---|
| `01_check_no_of_partitions.py` | Check the number of partitions |
| `02_repartition.py` | Repartition a DataFrame |
| `03_coalesce.py` | Reduce the number of partitions using `coalesce()` |

### 15. Data Skew

This module demonstrates a basic technique for mitigating data skew during distributed processing.

| File | Concept |
|---|---|
| `01_salting.py` | Salting technique for data skew |


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



