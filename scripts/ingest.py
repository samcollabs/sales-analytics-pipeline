import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

excel_data = pd.read_excel("data/raw/online_retail_ii.xlsx", sheet_name=None)

combined = pd.concat(excel_data.values(), ignore_index=True)

load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")

connection_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"
engine = create_engine(connection_url)

with engine.begin() as conn:
    conn.exec_driver_sql("CREATE SCHEMA IF NOT EXISTS raw;")
    conn.exec_driver_sql("DROP TABLE IF EXISTS raw.raw_sales CASCADE;")

combined.to_sql("raw_sales", engine, schema="raw", if_exists="replace", index=False)

print(f"Done! Loaded {len(combined)} rows into raw.raw_sales")