import pandas as pd
from sqlalchemy import create_engine

customers_df = pd.read_csv("data/raw/customers.csv")
products_df = pd.read_csv("data/raw/products.csv")

engine = create_engine(
    "postgresql://postgres:Welcome123%23@localhost:5432/ecommerce_db"
    )

customers_df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

products_df.to_sql(
    "products",
    engine,
    if_exists="replace",
    index=False
)