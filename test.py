#!/usr/bin/env python3
import os
import asyncio
from telethon import TelegramClient

# -----------------------------
# Environment Variables (set on Render)
# -----------------------------
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "")
MESSAGE_ID = int(os.getenv("MESSAGE_ID", "0"))

# -----------------------------
# Main
# -----------------------------
async def main():
    client = TelegramClient("temp_session", API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)

    try:
        msg = await client.get_messages(CHANNEL_USERNAME, ids=MESSAGE_ID)
        if msg.sticker:
            print("Sticker FILE ID:", msg.sticker.file.id)
        else:
            print("❌ No sticker found in this message")
    except Exception as e:
        print(f"❌ Error fetching message: {e}")
    finally:
        await client.disconnect()

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    asyncio.run(main())
