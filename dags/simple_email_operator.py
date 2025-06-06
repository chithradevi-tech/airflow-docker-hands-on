from airflow import DAG
from airflow.operators.email import EmailOperator
from datetime import datetime

with DAG('email_operator_example', start_date=datetime(2025, 6, 6)) as dag:
    task = EmailOperator(
        task_id='send_email',
        to='recipient@example.com',
        subject='Airflow Task Completed',
        html_content='<p>Your Airflow task has completed successfully.</p>'
    )
