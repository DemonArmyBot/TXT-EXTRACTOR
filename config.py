import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "24473318"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "e7dd0576c5ac0ff8f90971d6bb04c8f5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "742402153"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "742402153").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002327918459"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002327918459")  # Optional here you'll get all logs
