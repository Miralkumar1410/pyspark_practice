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
df.select("salary", F.round("salary", -3).alias("rounded"), F.ceil("salary").alias("ceil"), F.floor("salary").alias("floor"), F.abs("salary").alias("absolute"), F.sqrt("salary").alias("sqrt"), F.pow("salary", 2).alias("squared")).show()
spark.stop()
