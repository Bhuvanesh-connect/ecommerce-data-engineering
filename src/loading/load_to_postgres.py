import pandas as pd
from sqlalchemy import create_engine

orders_df = pd.read_csv("data/processed/orders_transformed.csv")

engine = create_engine(
    "postgresql://postgres:Welcome123%23@localhost:5432/ecommerce_db"
)

orders_df.to_sql("orders", engine, if_exists="replace", index=False)





