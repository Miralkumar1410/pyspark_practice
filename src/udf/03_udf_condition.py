from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("UDFCondition").master("local[*]").getOrCreate()

df = spark.createDataFrame([
    (1, 95000), (2, 65000), (3, 45000), (4, 30000)
], ["employee_id", "salary"])

@F.udf(returnType=StringType())
def salary_band(salary):
    if salary is None: return "Unknown"
    if salary >= 80000: return "High"
    if salary >= 50000: return "Medium"
    return "Low"

df.withColumn("salary_band", salary_band("salary")).show()
spark.stop()
