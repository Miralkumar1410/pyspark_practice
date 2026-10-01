from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("DataSkewSalting")
    .master("local[*]")
    .getOrCreate()
)

# ============================================================
# 1. Create a skewed dataset
# ============================================================

orders_data = [
    (1, "India", 1000),
    (2, "India", 1200),
    (3, "India", 1500),
    (4, "India", 1100),
    (5, "India", 1300),
    (6, "India", 1400),
    (7, "India", 1600),
    (8, "India", 1700),
    (9, "India", 1800),
    (10, "India", 1900),
    (11, "USA", 2000),
    (12, "USA", 2100),
    (13, "UK", 2200),
    (14, "Canada", 2300),
]

orders_df = spark.createDataFrame(
    orders_data,
    ["order_id", "country", "amount"]
)

print("Original data:")
orders_df.show()

print("Original country distribution:")
orders_df.groupBy("country").count().show()


# ============================================================
# 2. Create salt values
# ============================================================

# A hot/skewed key such as "India" receives multiple salt values.
# Other keys can also receive salt values for a uniform join strategy.

salt_count = 3

salted_orders = orders_df.withColumn(
    "salt",
    F.when(
        F.col("country") == "India",
        F.floor(F.rand(seed=42) * salt_count).cast("int")
    ).otherwise(F.lit(0))
)

print("Orders with salt:")
salted_orders.show()


# ============================================================
# 3. Create salted join key
# ============================================================

salted_orders = salted_orders.withColumn(
    "salted_country",
    F.concat(
        F.col("country"),
        F.lit("_"),
        F.col("salt")
    )
)

print("Salted join key:")
salted_orders.select(
    "order_id",
    "country",
    "salt",
    "salted_country",
    "amount"
).show()


# ============================================================
# 4. Create a dimension table
# ============================================================

country_data = [
    ("India", "IN"),
    ("USA", "US"),
    ("UK", "GB"),
    ("Canada", "CA"),
]

country_df = spark.createDataFrame(
    country_data,
    ["country", "country_code"]
)

print("Country dimension:")
country_df.show()


# ============================================================
# 5. Salt the dimension table
# ============================================================

# For the skewed key, create multiple copies so that
# each salted order key has a matching dimension key.

salt_values = spark.range(salt_count).withColumnRenamed(
    "id",
    "salt"
)

india_dimension = (
    country_df
    .filter(F.col("country") == "India")
    .crossJoin(salt_values)
)

other_dimensions = (
    country_df
    .filter(F.col("country") != "India")
    .withColumn("salt", F.lit(0))
)

salted_country_df = india_dimension.unionByName(
    other_dimensions
)

salted_country_df = salted_country_df.withColumn(
    "salted_country",
    F.concat(
        F.col("country"),
        F.lit("_"),
        F.col("salt")
    )
)

print("Salted dimension table:")
salted_country_df.show()


# ============================================================
# 6. Perform salted join
# ============================================================

result = (
    salted_orders
    .join(
        salted_country_df,
        on="salted_country",
        how="inner"
    )
    .select(
        "order_id",
        salted_orders["country"],
        "amount",
        "country_code"
    )
)

print("Result after salted join:")
result.show()


# ============================================================
# 7. Compare distribution after salting
# ============================================================

print("Salt distribution for the skewed key:")
salted_orders.filter(
    F.col("country") == "India"
).groupBy(
    "country",
    "salt"
).count().orderBy(
    "salt"
).show()


spark.stop()
