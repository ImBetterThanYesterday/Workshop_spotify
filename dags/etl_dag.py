from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl import read_csv, read_db, transform_spotify, grammys_transform_db, merge, load
#store

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 8),  # Update the start date to today or an appropriate date
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    'etl_dag',
    default_args=default_args,
    description='Workshop #2',
    schedule_interval='@daily',  # Set the schedule interval as per your requirements
) as dag:

    read_db = PythonOperator(
        task_id='read_db',
        python_callable=read_db,
    )

    grammys_transform_db = PythonOperator(
        task_id='grammys_transform_db',
        python_callable=grammys_transform_db,
        )
    
    read_csv = PythonOperator(
        task_id='read_csv',
        python_callable=read_csv,
    )

    transform_spotify = PythonOperator(
        task_id='transform_spotify',
        python_callable=transform_spotify,
        )
    
    merge = PythonOperator(
        task_id='merge',
        python_callable=merge,
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load,
    )

    # store = PythonOperator(
    #     task_id='store',
    #     python_callable=store,
    # )
    
    read_db >> grammys_transform_db >> merge
    read_csv >> transform_spotify >> merge >> load 
    #>> store