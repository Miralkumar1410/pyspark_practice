from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("SCDType3").master("local[*]").getOrCreate()

existing = spark.createDataFrame([
    (1,"Aarav","Delhi",None),
    (2,"Diya","Mumbai",None),
    (3,"Kabir","Bengaluru","Chennai")
], ["customer_id","customer_name","current_city","previous_city"])

incoming = spark.createDataFrame([
    (1,"Aarav","Raipur"),
    (2,"Diya","Pune"),
    (4,"Ananya","Hyderabad")
], ["customer_id","customer_name","new_city"])

updated = existing.alias("e").join(
    incoming.alias("i"), "customer_id"
).select(
    F.col("e.customer_id"),
    F.col("e.customer_name"),
    F.col("i.new_city").alias("current_city"),
    F.col("e.current_city").alias("previous_city")
)

unchanged = existing.join(
    incoming.select("customer_id"), "customer_id", "left_anti"
)

new_customers = incoming.join(
    existing.select("customer_id"), "customer_id", "left_anti"
).select(
    "customer_id",
    "customer_name",
    F.col("new_city").alias("current_city"),
    F.lit(None).cast("string").alias("previous_city")
)

updated.unionByName(unchanged).unionByName(new_customers)        .orderBy("customer_id").show(truncate=False)

spark.stop()
