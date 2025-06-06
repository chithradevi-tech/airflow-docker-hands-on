from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello from PythonOperator!")

with DAG('python_operator_example', start_date=datetime(2025, 6, 6)) as dag:
    task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello
    )
