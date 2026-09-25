from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("08_null_values_in_joins")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import col, coalesce, lit

orders = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\orders.csv"
)
customers = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\customers.csv"
)

# Standard equality joins do not match null with null.
result = orders.join(customers, on="customer_id", how="left")
result.select("order_id", "customer_id", "name").show()

# Identify rows with null customer_id.
orders.filter(col("customer_id").isNull()).show()

# Replace null with a readable label for display.
orders.withColumn(
    "customer_id_display",
    coalesce(col("customer_id").cast("string"), lit("Unknown"))
).show()

spark.stop()
