import pandas as pd 

from etls.reddit_etl import connect_reddit, extract_post, transform_data
from etls.reddit_etl import load_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT

def reddit_pipeline(file_name: str, subreddit: str, time_filter = 'day', limit=None):
    
    #connect to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    #extract data
    posts = extract_post(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)

    #transform raw data
    post_df = transform_data(post_df)

    #load to csv file
    filepath = f'{OUTPUT}/{file_name}.csv'
    load_to_csv(post_df, filepath)

    return filepath


