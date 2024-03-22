import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY 

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key=AWS_ACCESS_KEY_ID,
                               secret=AWS_SECRET_KEY)
        return s3
    except Exception as e:
        print('connect to s3 failed')


def create_if_not_exist(s3: s3fs.S3FileSystem, bucket:str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print('bucket made')
        else:
            print('bucket existed')
    except Exception as e:
        print('error when create bucket')


def upload_to_s3(s3: s3fs.S3FileSystem, filename: str, bucket: str, s3_filename: str):
    try: 
        s3.put(filename, bucket+'/raw data/'+s3_filename)
        print('file loaded successfully')
    except FileNotFoundError:
        print('error when try to find filename')
