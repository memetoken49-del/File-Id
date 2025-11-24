import asyncio
from telethon import TelegramClient
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH"))
BOT_TOKEN = os.getenv("BOT_TOKEN"))

CHANNEL = "BinancePumpSignals100"
MESSAGE_ID = 21191  # message that contains the sticker

async def main():
    client = TelegramClient("session", API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)
    
    msg = await client.get_messages(CHANNEL, ids=MESSAGE_ID)
    
    if msg.document:  # sticker is a document
        print("Sticker file_id:", msg.document.id)
        print("Access hash:", msg.document.access_hash)  # needed for sending via file_id
        print("DC id:", msg.document.dc_id)
    else:
        print("No document/sticker found in this message")
    
    await client.disconnect()

asyncio.run(main())
