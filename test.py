#!/usr/bin/env python3
import os
import asyncio
from telethon import TelegramClient

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "")  # no @
MESSAGE_ID = int(os.getenv("MESSAGE_ID", "0"))

async def main():
    client = TelegramClient("temp_session", API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)

    try:
        msg = await client.get_messages(CHANNEL_USERNAME, ids=MESSAGE_ID)
        file_id = None

        # Case 1: sticker object exists
        if getattr(msg, "sticker", None):
            if hasattr(msg.sticker, "file"):
                file_id = msg.sticker.file.id
            elif hasattr(msg.sticker, "document"):
                file_id = msg.sticker.document.id

        # Case 2: sticker is a document (common in channels)
        elif getattr(msg, "document", None):
            if msg.document.mime_type == "image/webp":
                file_id = msg.document.id

        if file_id:
            print("Sticker FILE ID:", file_id)
        else:
            print("❌ No sticker found in this message. Maybe it’s an animated sticker (tgs) or video sticker (webm).")
    
    except Exception as e:
        print(f"❌ Error fetching message: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
