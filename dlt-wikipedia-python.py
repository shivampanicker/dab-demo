# Databricks notebook source
import dlt
from pyspark.sql.functions import *


json_path = "/databricks-datasets/wikipedia-datasets/data-001/clickstream/raw-uncompressed-json/2015_2_clickstream.json"


@dlt.table(
    comment="The raw wikipedia clickstream dataset, ingested from /databricks-datasets."
)
def clickstream_raw():
    return (spark.read.format("json").load(json_path))

