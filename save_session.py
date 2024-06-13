from telethon import TelegramClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace these with your own values
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER') # Must include country code

# Name the session
session_name = os.getenv('SESSION_NAME')

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start(phone_number)
    print("Session saved!")

with client:
    client.loop.run_until_complete(main())