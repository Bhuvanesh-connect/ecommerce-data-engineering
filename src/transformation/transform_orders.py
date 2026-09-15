import pandas as pd

order_df = pd.read_csv("data/processed/orders_from_s3.csv")
order_df["order_total"] = order_df["quantity"] * order_df["price"]

print(order_df)


order_df.to_csv("data/processed/orders_transformed.csv", index=False)