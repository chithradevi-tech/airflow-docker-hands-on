from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime

with DAG('http_operator_example', start_date=datetime(2025, 6, 6)) as dag:
    task = SimpleHttpOperator(
        task_id='http_get_request',
        method='GET',
        http_conn_id='http_default',
        endpoint='api/v1/resource',
        headers={"Content-Type": "application/json"}
    )
