# ============================================================
# PySpark Basic Syntax
# ============================================================

# ============================================================
# 1. IMPORTS
# ============================================================

from pyspark.sql import SparkSession
from pyspark.sql import Row

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    LongType,
    ShortType,
    ByteType,
    FloatType,
    DoubleType,
    DecimalType,
    BooleanType,
    DateType,
    TimestampType,
    ArrayType,
    MapType
)


# ============================================================
# 2. CREATE SPARKSESSION
# ============================================================

spark = (
    SparkSession.builder
    .appName("PySparkBasicSyntax")
    .master("local[*]")
    .getOrCreate()
)


# ============================================================
# 3. CREATE DATAFRAME - BASIC SYNTAX
# ============================================================

data = [
    (1, "Aarav", "Delhi", 50000.0),
    (2, "Diya", "Mumbai", 60000.0),
    (3, "Kabir", "Bengaluru", 70000.0),
    (4, "Ananya", "Pune", 55000.0),
]

columns = [
    "id",
    "name",
    "city",
    "salary"
]

df = spark.createDataFrame(
    data,
    columns
)


# ============================================================
# 4. CREATE DATAFRAME USING ROW
# ============================================================

row_data = [
    Row(
        id=1,
        name="Aarav",
        city="Delhi",
        salary=50000.0
    ),
    Row(
        id=2,
        name="Diya",
        city="Mumbai",
        salary=60000.0
    ),
]

row_df = spark.createDataFrame(row_data)


# ============================================================
# 5. EXPLICIT SCHEMA
# ============================================================

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("city", StringType(), True),
    StructField("salary", DoubleType(), True)
])

schema_data = [
    (1, "Aarav", "Delhi", 50000.0),
    (2, "Diya", "Mumbai", 60000.0),
    (3, "Kabir", "Bengaluru", 70000.0),
]

schema_df = spark.createDataFrame(
    schema_data,
    schema=schema
)


# ============================================================
# 6. STRUCTTYPE
# ============================================================

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("city", StringType(), True),
    StructField("salary", DoubleType(), True),
])


# ============================================================
# 7. STRUCTFIELD
# ============================================================

id_field = StructField(
    "id",
    IntegerType(),
    False
)

name_field = StructField(
    "name",
    StringType(),
    False
)


# ============================================================
# 8. COMMON PYSPARK DATA TYPES - SYNTAX REFERENCE
# ============================================================

string_type = StringType()
integer_type = IntegerType()
long_type = LongType()
short_type = ShortType()
byte_type = ByteType()
float_type = FloatType()
double_type = DoubleType()
decimal_type = DecimalType()
boolean_type = BooleanType()
date_type = DateType()
timestamp_type = TimestampType()

array_type = ArrayType(StringType())
map_type = MapType(StringType(), StringType())


# ============================================================
# 9. NESTED SCHEMA SYNTAX
# ============================================================

nested_schema = StructType([
    StructField("id", IntegerType(), False),

    StructField(
        "name",
        StringType(),
        True
    ),

    StructField(
        "skills",
        ArrayType(StringType()),
        True
    ),

    StructField(
        "address",
        StructType([
            StructField("city", StringType(), True),
            StructField("state", StringType(), True)
        ]),
        True
    )
])


# ============================================================
# 10. CREATE DATAFRAME USING NESTED SCHEMA
# ============================================================

nested_data = [
    (
        1,
        "Aarav",
        ["Python", "PySpark"],
        ("Delhi", "Delhi")
    ),
    (
        2,
        "Diya",
        ["SQL", "Databricks"],
        ("Mumbai", "Maharashtra")
    )
]

nested_df = spark.createDataFrame(
    nested_data,
    schema=nested_schema
)


# ============================================================
# END
# ============================================================
