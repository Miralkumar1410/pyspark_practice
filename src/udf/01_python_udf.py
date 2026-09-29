from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("PythonUDF").master("local[*]").getOrCreate()

df = spark.createDataFrame([
    (1, "aarav sharma", "data engineer"),
    (2, "diya mehta", "data analyst"),
    (3, "kabir singh", "python developer")
], ["id", "name", "role"])

@F.udf(returnType=StringType())
def format_name(name):
    return name.title() if name else None

df.withColumn("formatted_name", format_name("name")).show()
spark.stop()
