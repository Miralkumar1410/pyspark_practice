from pyspark.sql import SparkSession
import pandas as pd

spark = (
    SparkSession.builder
    .appName("ApplyInPandasFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Aarav", "IT", 50000),
    (2, "Diya", "IT", 60000),
    (3, "Kabir", "HR", 55000),
    (4, "Ananya", "HR", 65000),
    (5, "Rohan", "Finance", 70000),
    (6, "Meera", "Finance", 75000),
]

df = spark.createDataFrame(
    data,
    ["id", "name", "department", "salary"]
)

# applyInPandas() applies a Pandas function to each group.
# Here, salary is increased by 10% within each department.

def add_increment(pdf: pd.DataFrame) -> pd.DataFrame:
    pdf = pdf.copy()
    pdf["incremented_salary"] = pdf["salary"] * 1.10
    return pdf

result_schema = """
    id long,
    name string,
    department string,
    salary long,
    incremented_salary double
"""

result = (
    df.groupBy("department")
      .applyInPandas(
          add_increment,
          schema=result_schema
      )
)

result.show()

spark.stop()
