from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta
import pandas as pd

RAW_FILE = "/opt/airflow/data/raw/daily_sales.csv"
CLEANED_FILE = "/opt/airflow/data/cleaned_daily_sales.csv"
PROCESSED_FILE = "/opt/airflow/data/processed/cleaned_sales.csv"

default_args = {
    "owner": "retail_team",
    "retries": 3,
    "retry_delay": timedelta(minutes=2),
}

def validate_sales_data():
    df = pd.read_csv(RAW_FILE)

    df["price"]=df["price"].astype(float) # Covert price into a float
    df["quantity"]=df["quantity"].astype(int) # Convert quantity into an integer
    df["price"] = df["price"].fillna(0) # Fill price nulls with 0
    df = df[df["price"] > 0] # Drop negative prices
    df["product"]=df["product"].str.title() # Convert first character of each product to uppercase
    df["city"]=df["city"].str.title() # Convert first character of each city to uppercase
    df["product"]=df["product"].str.strip() # Remove whitespaces in product

    df.to_csv(CLEANED_FILE, index=False)

    if df["price"].dtype != float:
        raise ValueError("Price is not a float value")
    
    if df["quantity"].dtype != int:
        raise ValueError("Quantity is not a integer value")

    if df.isnull().values.any():
        raise ValueError("Null values detected!")

    if (df["price"] < 0).any():
        raise ValueError("Negative prices found!")

    print("Validation successful!")

# def clean_sales_data():
#     df = pd.read_csv(RAW_FILE)

#     df["price"]=df["price"].astype(float) # Covert price into a float
#     df["quantity"]=df["quantity"].astype(int) # Convert quantity into an integer
#     df["price"] = df["price"].fillna(0) # Fill price nulls with 0
#     df = df[df["price"] > 0] # Drop negative prices
#     df["product"]=df["product"].str.title() # Convert first character of each product to uppercase
#     df["city"]=df["city"].str.title() # Convert first character of each city to uppercase
#     df["product"]=df["product"].str.strip() # Remove whitespaces in product

#     df.to_csv(CLEANED_FILE, index=False)

#     print("Cleaning successful!")

def transform_sales_data():
    df = pd.read_csv(CLEANED_FILE)

    df["total_sales"] = df["quantity"] * df["price"]

    df.to_csv(PROCESSED_FILE, index=False)

    print("Transformation completed!")

with DAG(
    dag_id="retail_ingestion_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args
) as dag:

    wait_for_file = FileSensor(
        task_id="wait_for_sales_file",
        filepath="data/raw/daily_sales.csv",
        poke_interval=30,
        timeout=300,
        mode="poke"
    )

    validate_task = PythonOperator(
        task_id="validate_sales_data",
        python_callable=validate_sales_data
    )
    
    # clean_task = PythonOperator(
    #     task_id="clean_sales_data",
    #     python_callable=clean_sales_data
    # )

    transform_task = PythonOperator(
        task_id="transform_sales_data",
        python_callable=transform_sales_data
    )

    wait_for_file >> validate_task >> transform_task
