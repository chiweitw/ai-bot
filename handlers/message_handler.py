from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from services.openai_service import generate_ai_response
from services.feeds import fetch_feeds

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    # Check if the user is asking for news
    data = None
    
    if "news" in user_message.lower():
        # Fetch news articles
        data = fetch_feeds()


    # Generate a response using OpenAI for other queries
    ai_reply = generate_ai_response(user_message, data)
    await update.message.reply_text(ai_reply)

handle_message = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)