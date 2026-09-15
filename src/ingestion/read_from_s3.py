import boto3
import pandas as pd

s3 = boto3.client("s3")
s3.download_file(
    "data-storage-s3-bucket-372815112385-ap-south-1-an",
    "raw/orders.csv",
    "data/processed/orders_from_s3.csv"
)

orders_df = pd.read_csv("data/processed/orders_from_s3.csv")

print(orders_df)