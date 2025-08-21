from telegram import Update
from telegram.ext import ContextTypes
from llm.model import init_llm  # Assuming init_llm is defined in model.py
import os

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    api_key = os.getenv("GOOGLE_API_KEY")
    llm = init_llm(api_key)

    # Generate a response from the language model
    response = llm.structured_predict(
        Character, prompt, text=user_message
    )

    await update.message.reply_text(response)