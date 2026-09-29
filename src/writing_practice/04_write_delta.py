from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("WriteDelta")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Aarav", "Delhi", 50000),
    (2, "Diya", "Mumbai", 60000),
    (3, "Kabir", "Bengaluru", 70000),
]

df = spark.createDataFrame(data, ["id", "name", "city", "salary"])

base_path = "output/write_delta"

# Delta Lake support is required for this file.

# 1. OVERWRITE
df.write.format("delta").mode("overwrite").save(
    f"{base_path}/overwrite"
)

# 2. APPEND
df.write.format("delta").mode("append").save(
    f"{base_path}/append"
)

# 3. IGNORE
df.write.format("delta").mode("ignore").save(
    f"{base_path}/ignore"
)

# 4. ERRORIFEXISTS
try:
    df.write.format("delta").mode("errorifexists").save(
        f"{base_path}/errorifexists"
    )
    print("Delta errorifexists write completed.")
except Exception as e:
    print("Delta errorifexists:", type(e).__name__)

print("Delta write modes: overwrite, append, ignore, errorifexists")
spark.stop()
