from pyrogram import Client, filters
from database.mongo import premium
from config import ADMINS

@Client.on_message(filters.command("add_premium") & filters.user(ADMINS))
async def add_premium(client, message):
    user_id = int(message.command[1])
    await premium.update_one(
        {"_id": user_id},
        {"$set": {"active": True}},
        upsert=True
    )
    await message.reply("💎 Premium added")