from pyrogram import Client, filters
from config import ADMINS

@Client.on_message(filters.command("ping") & filters.user(ADMINS))
async def ping(client, message):
    await message.reply("✅ Bot is alive")