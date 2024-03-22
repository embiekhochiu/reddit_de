from etls.aws_etl import connect_to_s3, create_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME

def upload_to_s3_pipeline(ti):

    filename = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')
    
    s3 = connect_to_s3()
    create_if_not_exist(s3, AWS_BUCKET_NAME)
    upload_to_s3(s3, filename, AWS_BUCKET_NAME, filename.split('/')[-1]) #retrieve only last filename
