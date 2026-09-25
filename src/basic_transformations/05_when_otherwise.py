from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("05_when_otherwise")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import col, when

df = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\customers.csv"
)

result = df.withColumn(
    "age_group",
    when(col("age") < 25, "Young")
    .when((col("age") >= 25) & (col("age") < 35), "Adult")
    .otherwise("Senior")
)

result.select("name", "age", "age_group").show()

spark.stop()
