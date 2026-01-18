from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI

client = AsyncIOMotorClient(MONGO_DB_URI)
db = client["AutoFilterBot"]

settings = db.settings
premium = db.premium
files = db.files