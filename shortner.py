from pyrogram import Client, filters
from database.mongo import settings
from config import ADMINS

@Client.on_message(filters.command("shortener_on") & filters.user(ADMINS))
async def short_on(client, message):
    await settings.update_one(
        {"_id": "SHORTENER"},
        {"$set": {"enabled": True}},
        upsert=True
    )
    await message.reply("🔗 Shortener Enabled")