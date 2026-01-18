from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from web import keep_alive

app = Client(
    "AutoFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

app.start()
keep_alive()
print("Bot Started Successfully")
idle()
