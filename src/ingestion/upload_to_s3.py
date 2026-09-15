import boto3

s3 = boto3.client("s3")


s3.upload_file(
    "data/raw/orders.csv",
    "data-storage-s3-bucket-372815112385-ap-south-1-an",
    "raw/orders.csv"
)