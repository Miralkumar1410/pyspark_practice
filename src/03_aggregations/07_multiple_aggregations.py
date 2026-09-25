from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("07_multiple_aggregations")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import count, sum, avg, min, max

orders = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\orders.csv"
)

result = orders.groupBy("department_id").agg(
    count("*").alias("total_orders"),
    sum("amount").alias("total_revenue"),
    avg("amount").alias("average_revenue"),
    min("amount").alias("minimum_order"),
    max("amount").alias("maximum_order")
)

result.orderBy("department_id").show()

spark.stop()
