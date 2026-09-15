import pandas as pd

def read_orders(file_path):
    return pd.read_csv(file_path)

orders_df = read_orders("data/raw/orders.csv")

print("All Orders -", orders_df)

orders_count = orders_df["order_id"].count()
print("Orders count -", orders_count)
print("Column Names -", orders_df.columns)
print("First 5 Orders -", orders_df.head(5))