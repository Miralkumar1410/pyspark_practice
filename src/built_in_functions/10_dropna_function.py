from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("DropnaFunction")
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

data_with_nulls = [
    (1, "Aarav", "Delhi", "IT", 50000),
    (2, "Diya", None, "HR", None),
    (3, "Kabir", "Delhi", "IT", 70000),
]

null_df = spark.createDataFrame(
    data_with_nulls,
    ["id", "name", "city", "department", "salary"]
)

result = null_df.dropna()
result.show()

result_selected = null_df.dropna(subset=["name", "salary"])
result_selected.show()
spark.stop()
