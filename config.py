import os
from dotenv import load_dotenv

load_dotenv()

REDDIT = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_SECRET"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
    "user_agent": "ColombianBank script"
}

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
