from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadParquet").master("local[*]").getOrCreate()

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"
df = spark.read.parquet(DATA_PATH + r"\\customers.parquet")

df.printSchema()
df.show(truncate=False)
spark.stop()
