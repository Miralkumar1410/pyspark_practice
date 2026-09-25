from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadCSV").master("local[*]").getOrCreate()

DATA_PATH = r"C:\Users\MiralkumarRatre\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\Documents\pyspark_practice_files\pyspark_practice\data"
df = (
    spark.read.format('csv').option("header", True).option("inferSchema", True)
    .load(DATA_PATH + r"\\customers.csv")
)

df.printSchema()
df.show(truncate=False)
spark.stop()
