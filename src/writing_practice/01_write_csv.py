from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("WriteCSV")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Aarav", "Delhi", 50000),
    (2, "Diya", "Mumbai", 60000),
    (3, "Kabir", "Bengaluru", 70000),
]

df = spark.createDataFrame(data, ["id", "name", "city", "salary"])

base_path = "output/write_csv"

# 1. OVERWRITE
df.write.mode("overwrite").option("header", True).csv(
    f"{base_path}/overwrite"
)

# 2. APPEND
df.write.mode("append").option("header", True).csv(
    f"{base_path}/append"
)

# 3. IGNORE
df.write.mode("ignore").option("header", True).csv(
    f"{base_path}/ignore"
)

# 4. ERRORIFEXISTS
# This mode throws an error if the target path already exists.
try:
    df.write.mode("errorifexists").option("header", True).csv(
        f"{base_path}/errorifexists"
    )
    print("CSV errorifexists write completed.")
except Exception as e:
    print("CSV errorifexists:", type(e).__name__)

print("CSV write modes: overwrite, append, ignore, errorifexists")
spark.stop()
