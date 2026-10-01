from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("DropDuplicatesFunction")
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

data_with_duplicates = [
    (1, "Aarav", "Delhi", "IT", 50000),
    (2, "Diya", "Mumbai", "HR", 60000),
    (2, "Diya", "Mumbai", "HR", 60000),
    (3, "Kabir", "Delhi", "IT", 70000),
]

duplicate_df = spark.createDataFrame(
    data_with_duplicates,
    ["id", "name", "city", "department", "salary"]
)

result = duplicate_df.dropDuplicates(["id"])
result.show()
spark.stop()
