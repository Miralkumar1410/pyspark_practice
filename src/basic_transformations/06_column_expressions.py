from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("06_column_expressions")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import col

df = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\customers.csv"
)

# Arithmetic expression.
df.withColumn("age_plus_ten", col("age") + 10).show()

# Comparison expression.
df.filter(col("age") >= 30).select("name", "age").show()

# Logical expression.
df.filter(
    (col("age") >= 25) & (col("city").isin("Delhi", "Mumbai", "Pune"))
).show()

# String expression.
df.filter(col("name").startswith("A")).show()

spark.stop()
