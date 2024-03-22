from airflow import DAG  
from datetime import datetime
import os
import sys
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.s3_pipeline import upload_to_s3_pipeline

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
    tags = ['reddit', 'etl', 'pipeline', 'aws']
)

#etl process
#reddit data extraction and transformation
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
upload_to_s3 = PythonOperator(
    task_id = 'upload_s3',
    python_callable = upload_to_s3_pipeline,
    op_kwargs={'task_id': 'upload_s3'},
    dag=dag
)

#sequence 
extract >> upload_to_s3