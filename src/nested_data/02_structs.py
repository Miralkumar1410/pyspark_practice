from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()
df=spark.createDataFrame([(1,"Aarav",("Delhi",110001)),(2,"Diya",("Mumbai",400001))],["id","name","address"])
df.printSchema()
df.select("name",F.col("address._1").alias("city"),F.col("address._2").alias("pincode")).show()
spark.stop()
