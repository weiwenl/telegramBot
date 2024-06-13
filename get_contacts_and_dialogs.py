from telethon import TelegramClient
import asyncio
from dotenv import load_dotenv
import os
from telethon.tl.functions.contacts import GetContactsRequest

# Load environment variables from .env file
load_dotenv()

# Replace these with your own values
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

# Name the session
session_name = os.getenv('SESSION_NAME')

client = TelegramClient(session_name, api_id, api_hash)

async def get_contacts_and_dialogs():
    await client.start()
    dialogs = []
    contacts = []

    # Fetch dialogs
    async for dialog in client.iter_dialogs():
        if dialog.is_user:
            dialogs.append({
                'id': dialog.id,
                'name': dialog.name or '',
                'username': dialog.entity.username or 'None',
                'phone': dialog.entity.phone or 'None'
            })

    # Fetch contacts
    result = await client(GetContactsRequest(hash=0))
    for user in result.users:
        user_entity = await client.get_entity(user.id)
        contacts.append({
            'id': user.id,
            'first_name': user_entity.first_name or '',
            'last_name': user_entity.last_name or '',
            'username': user_entity.username or 'None',
            'phone': user_entity.phone or 'None'
        })

    # Write dialogs to file with UTF-8 encoding
    with open('dialogs.txt', 'w', encoding='utf-8') as file:
        file.write('Dialogs:\n')
        for dialog in dialogs:
            file.write(f"ID: {dialog['id']}, Name: {dialog['name']}, Username: {dialog['username']}, Phone: {dialog['phone']}\n")

    # Write contacts to file with UTF-8 encoding
    with open('contacts.txt', 'w', encoding='utf-8') as file:
        file.write('Contacts:\n')
        for contact in contacts:
            file.write(f"ID: {contact['id']}, First Name: {contact['first_name']}, Last Name: {contact['last_name']}, Username: {contact['username']}, Phone: {contact['phone']}\n")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(get_contacts_and_dialogs())