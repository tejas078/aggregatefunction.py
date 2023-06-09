from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == '__main__':
    spark = SparkSession.builder.appName("Salary").getOrCreate()

    data = [(1, "Ram", 25, 20000), (2, "Sham", 29, 30000), (3, "Kiran", 31, 50000), (4, "Mina", 34, 14000)]
    header = ["id", "Name", "Age", "Salary"]

    input_rdd = spark.sparkContext.parallelize(data)
    input_df = input_rdd.toDF(header)

    input_df1 = input_df.select(max(input_df.Salary).alias("Salary"))
    input_df.join(input_df1, "Salary").select("Name", "Salary").show()
    input_df.filter(input_df.Age > 30).select("Name", "Age").show()
    input_df.select(sum(col("Salary"))).show()