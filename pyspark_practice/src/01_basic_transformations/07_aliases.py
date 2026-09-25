from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("07_aliases")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import col

df = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\customers.csv"
)

# Alias for a column.
df.select(
    col("customer_id").alias("id"),
    col("name").alias("customer_name")
).show()

# Alias for a calculated expression.
df.select(
    "name",
    (col("age") + 5).alias("projected_age")
).show()

spark.stop()
