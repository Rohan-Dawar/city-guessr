import praw, os

reddit = praw.Reddit(
    client_id = os.environ.get('client_id'),
    client_secret = os.environ.get('client_secret'),
    username = os.environ.get('username'),
    password = os.environ.get('password'),
    user_agent = os.environ.get('user_agent'))
