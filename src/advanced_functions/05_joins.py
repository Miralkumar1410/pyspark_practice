from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()
employees=spark.createDataFrame([(1,"Aarav",10),(2,"Diya",20),(3,"Kabir",10),(4,"Rohan",40)],["employee_id","employee_name","department_id"])
departments=spark.createDataFrame([(10,"Data Engineering"),(20,"Analytics"),(30,"HR")],["department_id","department_name"])
for join_type in ["inner","left","full","left_semi","left_anti"]:
    print(join_type.upper())
    employees.join(departments,"department_id",join_type).show()
spark.stop()
