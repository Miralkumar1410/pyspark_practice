from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("UDFVsBuiltin").master("local[*]").getOrCreate()

df = spark.createDataFrame([(1,"aarav"),(2,"diya"),(3,"kabir")], ["id","name"])

@F.udf(returnType=StringType())
def uppercase_udf(value):
    return value.upper() if value else None

df.withColumn("udf_result", uppercase_udf("name"))   .withColumn("builtin_result", F.upper("name"))   .show()

spark.stop()
