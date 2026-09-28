from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()
df = spark.createDataFrame([(1,"Aarav","2026-01-15"),(2,"Diya","2026-02-20"),(3,"Kabir","2026-03-10")],["id","name","joining_date"]).withColumn("joining_date",F.to_date("joining_date"))
df.select("*",F.year("joining_date").alias("year"),F.month("joining_date").alias("month"),F.dayofmonth("joining_date").alias("day"),F.date_format("joining_date","MMMM").alias("month_name"),F.date_add("joining_date",30).alias("after_30_days"),F.datediff(F.current_date(),"joining_date").alias("days_difference")).show()
spark.stop()
