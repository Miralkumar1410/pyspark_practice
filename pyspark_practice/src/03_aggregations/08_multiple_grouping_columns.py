from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("08_multiple_grouping_columns")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import count, sum

orders = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\orders.csv"
)

result = orders.groupBy(
    "department_id",
    "order_status"
).agg(
    count("*").alias("order_count"),
    sum("amount").alias("total_amount")
)

result.orderBy("department_id", "order_status").show()

spark.stop()
