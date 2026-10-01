from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("PivotFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Aarav", "Delhi", "IT", 50000),
    (2, "Diya", "Mumbai", "HR", 60000),
    (3, "Kabir", "Delhi", "IT", 70000),
    (4, "Ananya", "Pune", "Finance", 55000),
    (5, "Rohan", "Mumbai", "HR", 65000),
]

df = spark.createDataFrame(
    data,
    ["id", "name", "city", "department", "salary"]
)

sales_data = [
    ("Delhi", "Q1", 10000),
    ("Delhi", "Q2", 12000),
    ("Delhi", "Q3", 15000),
    ("Mumbai", "Q1", 9000),
    ("Mumbai", "Q2", 11000),
    ("Mumbai", "Q3", 13000),
    ("Pune", "Q1", 8000),
    ("Pune", "Q2", 9500),
    ("Pune", "Q3", 10500),
]

sales_df = spark.createDataFrame(
    sales_data,
    ["city", "quarter", "sales"]
)

result = (
    sales_df
    .groupBy("city")
    .pivot("quarter")
    .sum("sales")
)

result.show()
spark.stop()
