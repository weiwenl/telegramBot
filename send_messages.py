from telethon import TelegramClient
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace these with your own values
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Name the session
session_name = os.getenv('SESSION_NAME')

client = TelegramClient(session_name, api_id, api_hash)

async def send_message_to_dialogs(message):
    await client.start()

    # Read dialog IDs from dialogs.txt
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    dialog_ids = []
    for line in lines:
        if line.startswith("ID: "):
            parts = line.split(',')
            dialog_id = int(parts[0].split(': ')[1])
            dialog_ids.append(dialog_id)

    sent_dialogs = []
    failed_dialogs = []

    # Send message to each dialog ID with rate limiting
    for i, dialog_id in enumerate(dialog_ids):
        try:
            await client.send_message(dialog_id, message)
            print(f"Message sent to dialog ID: {dialog_id}")
            sent_dialogs.append(dialog_id)
        except Exception as e:
            print(f"Failed to send message to dialog ID: {dialog_id}. Error: {e}")
            failed_dialogs.append(dialog_id)

        # Rate limit to 20 messages per second
        if (i + 1) % 20 == 0:
            await asyncio.sleep(1)  # 1-second delay after every 20 messages

    # Write results to files
    with open('sent_contacts.txt', 'w', encoding='utf-8') as file:
        file.write('Sent Contacts:\n')
        for dialog_id in sent_dialogs:
            file.write(f"ID: {dialog_id}\n")

    with open('failed_contacts.txt', 'w', encoding='utf-8') as file:
        file.write('Failed Dialogs:\n')
        for dialog_id in failed_dialogs:
            file.write(f"ID: {dialog_id}\n")

if __name__ == "__main__":
    # Your custom message
    message = """
    Hey family and friends, 
    my tele got hacked earlier today between 4:50 PM and 5:00 PM. Sorry for the spam! Please don't click any links and leave any groups I added you to. I don't know who else got spammed, so I want to warn and notify all my Telegram contacts. Thanks to those who messaged me to check!
    """

    # Strip leading whitespace from each line
    message = '\n'.join(line.strip() for line in message.split('\n'))

    with client:
        client.loop.run_until_complete(send_message_to_dialogs(message))