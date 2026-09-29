from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("SCDType2").master("local[*]").getOrCreate()

existing = spark.createDataFrame([
    (1,"Aarav","Delhi","Gold","2025-01-01",None,True),
    (2,"Diya","Mumbai","Silver","2025-01-01",None,True),
    (3,"Kabir","Bengaluru","Bronze","2025-01-01",None,True)
], ["customer_id","customer_name","city","customer_type","effective_date","end_date","is_current"])

incoming = spark.createDataFrame([
    (1,"Aarav","Raipur","Gold"),
    (2,"Diya","Mumbai","Gold"),
    (4,"Ananya","Pune","Silver")
], ["customer_id","customer_name","city","customer_type"])

existing = existing.withColumn("effective_date", F.to_date("effective_date"))
today = F.current_date()

changes = existing.alias("e").join(
    incoming.alias("i"), "customer_id"
).where(
    F.col("e.is_current") &
    ((F.col("e.city") != F.col("i.city")) |
     (F.col("e.customer_type") != F.col("i.customer_type")))
).select("customer_id").distinct()

expired = existing.alias("e").join(
    changes.alias("c"), "customer_id", "left"
).withColumn(
    "end_date",
    F.when(F.col("c.customer_id").isNotNull() & F.col("e.is_current"),
           F.date_sub(today, 1)).otherwise(F.col("e.end_date"))
).withColumn(
    "is_current",
    F.when(F.col("c.customer_id").isNotNull() & F.col("e.is_current"),
           F.lit(False)).otherwise(F.col("e.is_current"))
).select(existing.columns)

new_versions = incoming.alias("i").join(
    changes.alias("c"), "customer_id"
).select(
    "i.customer_id","i.customer_name","i.city","i.customer_type"
).withColumn("effective_date", today)  .withColumn("end_date", F.lit(None).cast("date"))  .withColumn("is_current", F.lit(True))

new_customers = incoming.join(
    existing.select("customer_id").distinct(), "customer_id", "left_anti"
).withColumn("effective_date", today)  .withColumn("end_date", F.lit(None).cast("date"))  .withColumn("is_current", F.lit(True))

scd_type_2 = expired.unionByName(new_versions).unionByName(new_customers)
scd_type_2.orderBy("customer_id","effective_date").show(truncate=False)

spark.stop()
