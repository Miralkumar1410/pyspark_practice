from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
df=spark.createDataFrame([(1,'{"name":"Aarav","city":"Delhi","age":25}'),(2,'{"name":"Diya","city":"Mumbai","age":29}')],["id","json_string"])
schema=StructType([StructField("name",StringType()),StructField("city",StringType()),StructField("age",IntegerType())])
df.withColumn("person",F.from_json("json_string",schema)).select("id","person.name","person.city","person.age").show()
spark.stop()
