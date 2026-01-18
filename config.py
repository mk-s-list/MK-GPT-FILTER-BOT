import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
ADMINS = list(map(int, os.getenv("ADMINS", "").split()))

FILES_CHANNEL = int(os.getenv("FILES_CHANNEL"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))