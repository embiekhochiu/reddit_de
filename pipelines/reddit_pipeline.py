from utils.constants import CLIENT_ID, SECRET
from etls.reddit_etl import connect_reddit, extract_post

def reddit_pipeline(file_name: str, subreddit: str, time_filter = 'day', limit=None):
    
    #connect to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    #extract data
    posts = extract_post(instance, subreddit, time_filter, limit)
    #transform raw data
    #load to csv file