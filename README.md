# Telegram Message Sender

This project is a simple Telegram bot that sends a predefined message to all contacts. It ensures messages are sent with rate limiting to avoid being flagged as spam by Telegram. The project also keeps track of successfully sent and failed messages and maps remaining contacts that have not received the message due to errors.

## Background

This project was created to help notify all contacts in case of an emergency, such as a hacked account. The script was designed to be efficient, handling large contact lists while adhering to Telegram's rate limits.

## Features

- Send messages to all contacts listed in `dialogs.txt` and `contacts.txt`.
- Rate limiting to avoid hitting Telegram's limits.
- Log successfully sent and failed messages.
- Map remaining contacts and save them to `remaining.txt`.

## Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-message-sender.git
cd telegram-message-sender
```

### Step 2: Install Dependencies

```bash
pip install telethon python-dotenv
```

### Step 3: Obtain Telegram API Credentials
Create a Telegram App:
Go to [my.telegram.org](my.telegram.org) and log in with your Telegram account.
Click on "API Development Tools".
Create a new application by filling out the required fields. You will receive an api_id and an api_hash.

### Step 4: Set Up Environment Variables
Create a .env file in the root directory of the project and add your credentials:
```bash
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=your_phone_number
```

### Step 5: Save Session
Run the save_session.py script to authenticate and save the session:

```bash
python save_session.py
```

### Step 6: Send Messages
Edit dialogs.txt and contacts.txt with the IDs of the dialogs or contacts you want to send messages to. Then, run the script to send messages:

```bash
python send_message_to_dialogs.py
```

### Step 7: Handle Remaining Contacts
If there are any failed messages, you can map them to contacts and generate remaining.txt:

```bash
python map_remaining_contacts.py
```
