from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("01_groupBy")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

orders = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\orders.csv"
)

# Group rows by customer_id.
grouped = orders.groupBy("customer_id")

# A groupBy is usually followed by an aggregation.
grouped.count().show()

spark.stop()
