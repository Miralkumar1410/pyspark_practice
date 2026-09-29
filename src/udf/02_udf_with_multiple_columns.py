from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import DoubleType

spark = SparkSession.builder.appName("UDFMultipleColumns").master("local[*]").getOrCreate()

df = spark.createDataFrame([
    (1, 50000.0, 10.0),
    (2, 65000.0, 12.0),
    (3, 80000.0, 15.0)
], ["employee_id", "salary", "bonus_percent"])

@F.udf(returnType=DoubleType())
def calculate_bonus(salary, percent):
    return salary * percent / 100 if salary is not None and percent is not None else None

df.withColumn("bonus_amount", calculate_bonus("salary", "bonus_percent"))   .withColumn("total_compensation", F.col("salary") + F.col("bonus_amount"))   .show()
spark.stop()
