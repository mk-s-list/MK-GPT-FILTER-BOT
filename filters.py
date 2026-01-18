from pyrogram import Client, filters
from database.mongo import files

@Client.on_message(filters.text & ~filters.command)
async def auto_filter(client, message):
    query = message.text.lower()
    result = await files.find_one({"name": {"$regex": query, "$options": "i"}})
    if result:
        await message.reply_document(result["file_id"], caption=result["name"])
    else:
        await message.reply("❌ File not found")