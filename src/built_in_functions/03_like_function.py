from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("LikeFunction")
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

result = df.where(F.col("name").like("A%"))
result.show()
spark.stop()
