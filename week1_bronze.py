from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder.appName("EchoChain") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

df = spark.read.csv(
    "data/scraped_ebay_listings.csv",
    header=True,
    inferSchema=True
)

df.show(5)

df.printSchema()

print(df.count())

from pyspark.sql.functions import col, isnull

df.select(
    [isnull(col(c)).alias(c) for c in df.columns]
).show()

df.write.format("delta") \
    .mode("overwrite") \
    .save("delta/bronze/laptop_listings")

bronze = spark.read.format("delta").load("delta/bronze/laptop_listings")

bronze.show(5)

bronze.describe().show()

bronze.groupBy("condition").count().show()

bronze.groupBy("location").count().show()