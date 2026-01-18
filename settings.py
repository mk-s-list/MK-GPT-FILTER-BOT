from pyrogram import Client, filters
from database.mongo import settings
from config import ADMINS

@Client.on_message(filters.command("set_start") & filters.user(ADMINS))
async def set_start(client, message):
    text = message.text.split(None, 1)[1]
    await settings.update_one(
        {"_id": "START"},
        {"$set": {"text": text}},
        upsert=True
    )
    await message.reply("✅ Start message updated")