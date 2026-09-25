from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("04_count")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import count

orders = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\orders.csv"
)

# Count all rows in each department.
orders.groupBy("department_id").agg(
    count("*").alias("row_count")
).show()

# Count only non-null customer_id values.
orders.groupBy("department_id").agg(
    count("customer_id").alias("non_null_customer_count")
).show()

spark.stop()
