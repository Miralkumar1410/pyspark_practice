from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SCDType1").master("local[*]").getOrCreate()

existing = spark.createDataFrame([
    (1,"Aarav","Delhi","Gold"),
    (2,"Diya","Mumbai","Silver"),
    (3,"Kabir","Bengaluru","Bronze")
], ["customer_id","customer_name","city","customer_type"])

incoming = spark.createDataFrame([
    (1,"Aarav","Raipur","Gold"),
    (2,"Diya","Mumbai","Gold"),
    (4,"Ananya","Pune","Silver")
], ["customer_id","customer_name","city","customer_type"])

unchanged = existing.join(
    incoming.select("customer_id"), "customer_id", "left_anti"
)

scd_type_1 = unchanged.unionByName(incoming)

scd_type_1.orderBy("customer_id").show()
spark.stop()
