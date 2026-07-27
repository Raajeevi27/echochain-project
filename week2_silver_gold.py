from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EchoChain Week2") \
    .getOrCreate()

df = spark.read.csv(
    "data/scraped_ebay_listings.csv",
    header=True,
    inferSchema=True
)

df.show(5)

from pyspark.sql.functions import *

clean_df = df.dropDuplicates()

clean_df = clean_df.fillna({
    "condition": "Unknown",
    "location": "Unknown"
})

clean_df = clean_df.withColumn(
    "title",
    trim(lower(col("title")))
)

clean_df.show()

from pyspark.sql.functions import regexp_extract

clean_df = clean_df.withColumn(
    "SKU",
    regexp_extract(
        col("title"),
        r"(latitude\s*\d+|elitebook\s*\d+|thinkpad\s*[a-z0-9]+)",
        1
    )
)

clean_df.select("title","SKU").show()

clean_df.write \
    .mode("overwrite") \
    .format("parquet") \
    .save("data/bronze/ebay_listings")

silver_df = clean_df.filter(
    col("SKU") != ""
)

silver_df.write \
    .mode("overwrite") \
    .format("parquet") \
    .save("silver/ebay_listings")

bom = spark.createDataFrame([
    ("Latitude 5420","Dell",900,30),
    ("EliteBook 840","HP",950,18),
    ("ThinkPad T480","Lenovo",850,25)
],[
    "SKU",
    "Brand",
    "Manufacturing_Cost",
    "Warranty_Failures"
])
bom = bom.withColumn("SKU", lower(col("SKU"))) 

joined = silver_df.join(
    bom,
    on="SKU",
    how="left"
)

joined.show()

joined.write \
    .mode("overwrite") \
    .format("parquet") \
    .save("gold/echochain")

joined.coalesce(1).write.mode("overwrite").option("header", True).csv("data/gold/echochain_powerbi_csv")