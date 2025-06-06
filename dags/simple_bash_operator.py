from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('bash_operator_example', start_date=datetime(2025, 6, 6)) as dag:
    task = BashOperator(
        task_id='echo_task',
        bash_command='echo "Hello from BashOperator!"'
    )
