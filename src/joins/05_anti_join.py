from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("05_anti_join")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

customers = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\customers.csv"
)
orders = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\orders.csv"
)

result = customers.join(orders, on="customer_id", how="left_anti")
result.show()

spark.stop()
