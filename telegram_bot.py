import os
import django
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internship_project.settings")
django.setup()

from api.models import TelegramUser

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    username = update.message.from_user.username
    chat_id = update.message.chat_id

    # Log the interaction to terminal
    print(f"Received /start command from Telegram user: {username} (chat_id: {chat_id})")

    # Save or notify user
    if not TelegramUser.objects.filter(username=username).exists():
        TelegramUser.objects.create(username=username, chat_id=chat_id)
        update.message.reply_text(f"Hi {username}, you've been registered!")
    else:
        update.message.reply_text(f"Hi {username}, you're already registered!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    print("Bot is polling...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
