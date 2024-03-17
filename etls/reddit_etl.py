import praw
from praw import Reddit
import sys
import pandas as pd
from utils.constants import POST_FIELD

def connect_reddit(client_id, secret_key, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id = client_id,
                             client_secret = secret_key,
                             user_agent = user_agent,)
        print('reddit connection successful')
        return reddit
    except Exception as e:
        print(f'reddit connection failed: {e}')
        sys.exit(1)

def extract_post(reddit_instance: Reddit, subreddit: str, time_filter: str, limit = None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter =time_filter, limit=limit)
    
    post_list = []
    
    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELD}
        post_list.append(post)

    return post_list

def transform_data(post_df: pd.DataFrame):
    post_df['author_fullname'] = post_df['author_fullname'].astype(str)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['created'] = pd.to_datetime(post_df['created'], unit='s')
    
    return post_df

def load_to_csv(post_df: pd.DataFrame, pathfile: str):
    post_df.to_csv(pathfile, index = False)




        