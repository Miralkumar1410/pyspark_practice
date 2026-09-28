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
df.select(F.trim("name").alias("trimmed"), F.upper("name").alias("upper"), F.lower("name").alias("lower"), F.length("name").alias("length"), F.split(F.trim("name"), " ").getItem(0).alias("first_name"), F.regexp_replace("name", " ", "_").alias("replaced")).show()
spark.stop()
