from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("SortFunction")
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

result = df.sort(F.col("salary").desc())
result.show()

result_multiple = df.sort(
    F.col("city").asc(),
    F.col("salary").desc()
)
result_multiple.show()
spark.stop()
