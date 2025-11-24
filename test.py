import asyncio
from telethon import TelegramClient

API_ID = int("YOUR_API_ID")
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

CHANNEL_USERNAME = "BinancePumpSignals100"  # the channel
MESSAGE_ID = 21191                           # the message with your sticker

async def main():
    client = TelegramClient("temp_session", API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)
    
    msg = await client.get_messages(CHANNEL_USERNAME, ids=MESSAGE_ID)
    if msg.sticker:
        print("Sticker FILE ID:", msg.sticker.file.id)
    else:
        print("No sticker found in this message")
    
    await client.disconnect()

asyncio.run(main())
