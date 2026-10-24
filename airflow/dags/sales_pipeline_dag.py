from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "teller",
    "retries": 1,
}

with DAG(
    dag_id="sales_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    ingest = BashOperator(
        task_id="ingest_data",
        bash_command="cd /opt/sales-pipeline && python scripts/ingest.py",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/sales-pipeline/sales_analytics && dbt run --profiles-dir /opt/sales-pipeline/airflow/dbt_profiles",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/sales-pipeline/sales_analytics && dbt test --profiles-dir /opt/sales-pipeline/airflow/dbt_profiles",
    )

    ingest >> dbt_run >> dbt_test