# Telegram Joke Bot 🤖😄

A Telegram bot that sends random dad jokes every 5 minutes 
to subscribed users. Built with Python and the Telegram Bot API.

## Features
- Sends random jokes every 5 minutes automatically
- Subscribe with /joke command
- Unsubscribe with /stop command
- Fetches fresh jokes from public joke API
- Supports multiple subscribers simultaneously

## Commands
- /start - Welcome message
- /joke - Get a joke and subscribe to alerts
- /stop - Unsubscribe from joke alerts
- /help - Show available commands

## Installation

1. Clone the repository:
git clone https://github.com/joram009/telegram-joke-bot.git

2. Install dependencies:
pip install -r requirements.txt

3. Set up your bot token:
- Copy token_config.example.py
- Rename to token_config.py
- Add your Telegram bot token from BotFather

4. Run the bot:
python telegram_joke_bot.py

## Technologies Used
- Python
- python-telegram-bot v22.7
- Requests
- Official Joke API

## Author
Joram Onsoti
Nairobi, Kenya
github.com/joram009
