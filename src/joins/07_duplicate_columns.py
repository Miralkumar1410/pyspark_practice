from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("07_duplicate_columns")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import col

orders = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\orders.csv"
)
employees = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\employees.csv"
)

o = orders.alias("o")
e = employees.alias("e")

joined = o.join(
    e,
    col("o.department_id") == col("e.department_id"),
    "inner"
)

# Qualify columns using aliases.
joined.select(
    col("o.order_id"),
    col("o.department_id").alias("order_department_id"),
    col("e.department_id").alias("employee_department_id"),
    col("e.employee_name"),
    col("o.amount")
).show()

spark.stop()
