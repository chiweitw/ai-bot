from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from services.openai_service import generate_ai_response
from services.service_registry import get_relevant_services

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # Step 1: Determine relevant services
    relevant_services = get_relevant_services(user_message)

    # Step 2: Fetch data from relevant services
    data = ""
    for service in relevant_services:
        service_data = service()
        if service_data:
            data += f"\n{service_data}"

    # Step 3: Generate a response with or without additional data
    ai_reply = generate_ai_response(user_message, data=data if data else None)

    await update.message.reply_text(ai_reply)

handle_message = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)