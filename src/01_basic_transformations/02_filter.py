from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("02_filter")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import col

df = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\customers.csv"
)

# Customers whose age is greater than 28.
result = df.filter(col("age") > 28)

result.show()

# Multiple conditions: age >= 25 AND city is not Mumbai.
result = df.filter((col("age") >= 25) & (col("city") != "Mumbai"))

result.show()

spark.stop()
