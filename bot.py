import logging
from telegram import Update
from telegram import (
    Update,
    User,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    BotCommand
)
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    AIORateLimiter,
    filters
)
import openai
import requests
import os
from dotenv import load_dotenv
from handlers.command_handler import start
from handlers.message_handler import handle_message

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("/tweets", "Get some tweets"),
        # BotCommand("/help", "Show help message"),
    ])


def run_bot() -> None:
    """Start the bot."""

    application = (
        ApplicationBuilder()
        .token(os.getenv('TELEGRAM_TOKEN'))
        .concurrent_updates(True)
        .rate_limiter(AIORateLimiter(max_retries=5))
        .post_init(post_init)
        .build()
    )

    allowed_telegram_usernames = os.getenv('ALLOWED_TELEGRAM_USERNAMES').split(',')

    # add handlers
    user_filter = filters.ALL
    if len(allowed_telegram_usernames) > 0:
        usernames = [x for x in allowed_telegram_usernames if isinstance(x, str)]
        any_ids = [x for x in allowed_telegram_usernames if isinstance(x, int)]
        user_ids = [x for x in any_ids if x > 0]
        group_ids = [x for x in any_ids if x < 0]
        user_filter = filters.User(username=usernames) | filters.User(user_id=user_ids) | filters.Chat(chat_id=group_ids)


    # Create the Updater and pass it your bot's token.
    # updater = Updater(os.getenv('TELEGRAM_TOKEN'))

    # Get the dispatcher to register handlers
    # dispatcher = updater.dispatcher

    # Register command handlers
    application.add_handler(start)
    application.add_handler(handle_message)
    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    run_bot()
