from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
import pandas as pd

PROCESSED_FILE = "/opt/airflow/data/processed/cleaned_sales.csv"

default_args = {
    "owner": "analytics_team",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

def check_sales(**context):

    df = pd.read_csv(PROCESSED_FILE)

    total_sales = df["total_sales"].sum()

    print(f"Total Sales = {total_sales}")

    # if total_sales < 100000:
    #     context["ti"].xcom_push(
    #         key="alert_message",
    #         value=f"ALERT: Sales dropped to {total_sales}"
    #     )    

    context["ti"].xcom_push(
        key="total_sales",
        value=total_sales
    )

    if total_sales < 100000:
        return "alert_email"
    
    return "report_email"

with DAG(
    dag_id="retail_alert_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    sales_check_task = BranchPythonOperator(
        task_id="check_sales",
        python_callable=check_sales
    )

    # send_email = EmailOperator(
    #     task_id="send_email_alert",
    #     to="manager@gmail.com",
    #     subject="Retail Sales Alert",
    #     html_content="""
    #     <h3>Sales Alert Triggered</h3>
    #     <p>Please check today's sales report.</p>
    #     """,
    #     retries=3,
    # )

    send_alert_email = EmailOperator(
        task_id="alert_email",
        to="vicky@gmail.com",
        subject="Retail Sales Alert",
        html_content="""
        <h3>Sales Alert Triggered</h3>
        <h4>ALERT! Yesterday, the total sales were {{ ti.xcom_pull(task_ids='check_sales', key='total_sales') }}</h4>
        <p>The total sales are below.</p>
        <p>Please check today's sales report.</p>
        """,
        retries=3,
    )

    send_report_email = EmailOperator(
        task_id="report_email",
        to="vicky@gmail.com",
        subject="Retail Sales Report",
        html_content="""
        <h3>Sales Report</h3>
        <h4>Yesterday, the total sales were {{ ti.xcom_pull(task_ids='check_sales', key='total_sales') }}</h4>
        <p>The total sales are as expected.</p
        """,
        retries=3,
    )

    sales_check_task >> [send_alert_email, send_report_email]
