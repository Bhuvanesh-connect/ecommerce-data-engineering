from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def ingest_orders():
    print("Ingesting orders...")


def transform_orders():
    print("Transforming orders...")


def validate_orders():
    print("Validating orders...")


def load_postgres():
    print("Loading data into PostgreSQL...")


with DAG(
    dag_id="ecommerce_pipeline",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
) as dag:

    ingest = PythonOperator(
        task_id="ingest_orders",
        python_callable=ingest_orders,
    )

    transform = PythonOperator(
        task_id="transform_orders",
        python_callable=transform_orders,
    )

    validate = PythonOperator(
        task_id="validate_orders",
        python_callable=validate_orders,
    )

    load = PythonOperator(
        task_id="load_postgres",
        python_callable=load_postgres,
    )

    ingest >> transform >> validate >> load