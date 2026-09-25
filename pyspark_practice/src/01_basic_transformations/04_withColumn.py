from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("04_withColumn")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import col, lit

df = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\customers.csv"
)

# Create a new column.
result = df.withColumn("age_after_five_years", col("age") + 5)

# Create a constant column.
result = result.withColumn("country", lit("India"))

result.show()

# Replace an existing column.
result = result.withColumn("age", col("age") + 1)
result.show()

spark.stop()
