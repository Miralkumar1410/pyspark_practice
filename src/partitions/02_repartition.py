from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Repartition")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Aarav", "Delhi", 50000),
    (2, "Diya", "Mumbai", 60000),
    (3, "Kabir", "Delhi", 70000),
    (4, "Ananya", "Pune", 55000),
    (5, "Rohan", "Mumbai", 65000),
    (6, "Meera", "Pune", 58000),
    (7, "Arjun", "Delhi", 62000),
    (8, "Sara", "Mumbai", 59000),
]

df = spark.createDataFrame(
    data,
    ["id", "name", "city", "salary"]
)

# repartition() increases or decreases partitions using a shuffle.
print("Before repartition:", df.rdd.getNumPartitions())

repartitioned_df = df.repartition(4)

print("After repartition:", repartitioned_df.rdd.getNumPartitions())

repartitioned_df.show()


spark.stop()
