from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG('postgres_operator_example', start_date=datetime(2025, 6, 6)) as dag:
    task = PostgresOperator(
        task_id='create_table',
        sql="""
            CREATE TABLE IF NOT EXISTS example_table (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100)
            );
        """,
        postgres_conn_id='postgres_default'
    )
