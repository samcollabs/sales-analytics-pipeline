# Sales Analytics Pipeline

An end-to-end data pipeline that ingests raw e-commerce sales data, 
cleans it, and builds business-ready summary tables using Python, 
PostgreSQL, and dbt.

## Architecture
raw Excel file → Python/pandas ingestion → PostgreSQL (raw schema) 
→ dbt staging model (cleaned) → dbt mart model (daily revenue summary)

## Tech stack
- Python (pandas, sqlalchemy)
- PostgreSQL
- dbt (data build tool)
- Git

## Data quality issues found and handled
- 6,207 rows with invalid prices (excluded)
- 22,950 return transactions (flagged, not deleted)
- 243,007 transactions with missing customer ID (defaulted to -1, made explicit)

## How to run
1. Set up `.env` with your Postgres credentials
2. `pip install -r requirements.txt`
3. `python scripts/ingest.py`
4. `cd sales_analytics && dbt run && dbt test`