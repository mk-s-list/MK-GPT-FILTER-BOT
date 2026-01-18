from pyrogram import Client, filters
from database.mongo import settings

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    data = await settings.find_one({"_id": "START"})
    text = data["text"] if data else "👋 Welcome to Auto Filter Bot"
    await message.reply_text(text)