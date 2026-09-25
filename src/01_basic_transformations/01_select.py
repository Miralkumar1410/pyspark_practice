from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("01_select")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

df = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\customers.csv"
)

print("Original DataFrame:")
df.show()

# Select specific columns.
selected_df = df.select("customer_id", "name", "city")

print("Selected columns:")
selected_df.show()

# Select using column expressions.
from pyspark.sql.functions import col

df.select(col("name"), col("age")).show()

spark.stop()
