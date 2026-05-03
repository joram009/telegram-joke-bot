from telegram import Update
from token_config import token
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests


chat_id = []
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your Telegram bot. How can I assist you today? if you want to receive jokes every 5 mins, please click -> /joke command!')

def get_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        jokes = response.json()
        return f"{jokes['setup']} - {jokes['punchline']}"
    else:
        return "Sorry, the jokes are on you."


async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    joke_text = get_joke()
    await update.message.reply_text('Here is a joke for you:')
    await update.message.reply_text(joke_text)
    if update.effective_chat.id not in chat_id:
        chat_id.append(update.effective_chat.id)


async def alert_function(context: ContextTypes.DEFAULT_TYPE) -> None:
    for chat in chat_id:
        await context.bot.send_message(chat_id=chat, text='Here is a joke for you:')
        await context.bot.send_message(chat_id=chat, text=get_joke())


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_chat.id in chat_id:
        chat_id.remove(update.effective_chat.id)
        await update.message.reply_text('You have stopped receiving jokes every 5 mins.')
    else:
        await update.message.reply_text('You are not currently receiving jokes every 5 mins.')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('I am here to help you! You can use /start to begin and /joke to receive a joke every 5 mins,to stop receiving jokes, use /stop and /help to see this message again.')


def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help)) 
    application.add_handler(CommandHandler('joke', joke))
    application.add_handler(CommandHandler('stop', stop))
    application.job_queue.run_repeating(alert_function, interval=300)
    application.run_polling()


if __name__ == '__main__':
    main()