import praw
from praw import Reddit
import sys

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
    
    print(posts)


        