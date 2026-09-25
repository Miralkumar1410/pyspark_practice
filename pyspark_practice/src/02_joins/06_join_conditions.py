from pyspark.sql import SparkSession

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("06_join_conditions")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"

from pyspark.sql.functions import col

orders = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\orders.csv"
)
departments = spark.read.option("header", True).option("inferSchema", True).csv(
    DATA_PATH + r"\departments.csv"
)

result = orders.join(
    departments,
    orders["department_id"] == departments["department_id"],
    "inner"
)

result.select(
    orders["order_id"],
    orders["department_id"],
    departments["department_name"],
    orders["amount"]
).show()

spark.stop()
