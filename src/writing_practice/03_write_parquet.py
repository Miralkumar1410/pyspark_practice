from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("WriteParquet")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Aarav", "Delhi", 50000),
    (2, "Diya", "Mumbai", 60000),
    (3, "Kabir", "Bengaluru", 70000),
]

df = spark.createDataFrame(data, ["id", "name", "city", "salary"])

base_path = "output/write_parquet"

# 1. OVERWRITE
df.write.mode("overwrite").parquet(
    f"{base_path}/overwrite"
)

# 2. APPEND
df.write.mode("append").parquet(
    f"{base_path}/append"
)

# 3. IGNORE
df.write.mode("ignore").parquet(
    f"{base_path}/ignore"
)

# 4. ERRORIFEXISTS
try:
    df.write.mode("errorifexists").parquet(
        f"{base_path}/errorifexists"
    )
    print("Parquet errorifexists write completed.")
except Exception as e:
    print("Parquet errorifexists:", type(e).__name__)

print("Parquet write modes: overwrite, append, ignore, errorifexists")
spark.stop()
