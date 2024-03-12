from airflow import DAG  
from datetime import datetime
import os
import sys
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'embiekhochiu',
    'start_date': datetime(2024, 3, 7),
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='reddit_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup = False,
    tags = ['reddit', 'etl', 'pipeline']
)

#etl process
#reddit data extraction
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_data_{file_postfix}',
        'subreddit': 'DE',
        'time_filter': 'day',
        'limit' : 100
    },
    dag=dag
)

#upload data to s3 aws