from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("EcommerceOrders") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .getOrCreate()

orders_df = spark.read.csv(
    "data/raw/orders.csv",
    header=True,
    inferSchema=True
)

orders_df = orders_df.withColumn(
    "order_total",
    col("quantity") * col("price")
)

orders_df.show()


filtered_orders = orders_df.filter(
    col("order_total") > 3000
)

filtered_orders.show()

filtered_orders.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("data/processed/spark_orders")

spark.stop()