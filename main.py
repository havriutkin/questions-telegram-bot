"""
Telegram Bot with Google Sheets Integration

Description:
    This Python project implements a Telegram bot that allows users to submit questions, 
    and it automatically stores these questions in a Google Sheets spreadsheet.

Features:
    - Telegram bot integration using the python-telegram-bot library.
    - Authentication and access to Google Sheets API for data storage.
    - A '/start' command to initiate the bot and welcome users.
    - Message handling to capture and record user questions in real-time.
    - Append user questions to a specified Google Sheets worksheet.
    - User-friendly confirmation messages upon successful question submission.

Usage:
    1. Start the bot by sending the '/start' command.
    2. Send questions or inquiries to the bot.
    3. The bot will record the questions and store them in a Google Sheets document.
    4. Users receive confirmation messages for successful submissions.

Dependencies:
    - PTB: Python wrapper for the Telegram Bot API.
    - Gspread: Python library to interact with Google Sheets API.
    - Google Sheets API credentials file ('your-credentials.json').

    
Authors:
    - Vladyslav Havriutkin
    - John Smith (He knows how to use branches!)
    - [Enter your name here]
"""

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    ConversationHandler,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start callback function, greets a user"""


if __name__ == "__main__":
    application = ApplicationBuilder().token("TOKEN").build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()
