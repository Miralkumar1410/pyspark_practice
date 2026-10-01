from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("UnionFunction")
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

data1 = [
    (6, "Meera", "Chennai", "IT", 58000),
    (7, "Arjun", "Kolkata", "Finance", 62000),
]
data2 = [
    (8, "Sara", "Jaipur", "HR", 59000),
    (9, "Ishaan", "Surat", "IT", 61000),
]

df1 = spark.createDataFrame(
    data1, ["id", "name", "city", "department", "salary"]
)
df2 = spark.createDataFrame(
    data2, ["id", "name", "city", "department", "salary"]
)

result = df1.union(df2)
result.show()
spark.stop()
