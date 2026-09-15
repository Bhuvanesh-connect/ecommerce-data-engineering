import pandas as pd

orders_df = pd.read_csv("data/processed/orders_transformed.csv")

# Check for missing values
missing_values = orders_df.isnull().sum()

# Check for invalid quantity
invalid_quantity = orders_df["quantity"] <= 0

# Check for invalid price
invalid_price = orders_df["price"] <= 0

if missing_values.any():
    print("❌ Data Quality Failed: Missing values found")
    print(missing_values)

elif invalid_quantity.any():
    print("❌ Data Quality Failed: Invalid quantity found")

elif invalid_price.any():
    print("❌ Data Quality Failed: Invalid price found")

else:
    print("✅ Data Quality Passed")