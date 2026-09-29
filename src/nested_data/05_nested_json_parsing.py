from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
df=spark.createDataFrame([(1,'{"customer":{"name":"Aarav","address":{"city":"Delhi","pincode":110001}}}')],["id","json_string"])
schema=StructType([StructField("customer",StructType([StructField("name",StringType()),StructField("address",StructType([StructField("city",StringType()),StructField("pincode",IntegerType())]))]))])
p=df.withColumn("data",F.from_json("json_string",schema))
p.select("id",F.col("data.customer.name").alias("customer_name"),F.col("data.customer.address.city").alias("city"),F.col("data.customer.address.pincode").alias("pincode")).show()
spark.stop()
