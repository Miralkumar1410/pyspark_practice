from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()
df = spark.createDataFrame([
    (1, "Aarav", "Data", 70000, ["Python", "SQL"]),
    (2, "Diya", "Data", 85000, ["PySpark", "SQL"]),
    (3, "Kabir", "HR", 60000, ["Python", "Spark"]),
    (4, "Rohan", "HR", 65000, ["SQL", "Excel"]),
], ["id", "name", "department", "salary", "skills"])
df.select(F.count("*").alias("count"),F.sum("salary").alias("sum"),F.avg("salary").alias("avg"),F.min("salary").alias("min"),F.max("salary").alias("max")).show()
df.groupBy("department").agg(F.count("*").alias("count"),F.sum("salary").alias("total"),F.avg("salary").alias("average")).show()
spark.stop()
