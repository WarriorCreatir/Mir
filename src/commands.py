from loguru import logger
from telegram import Update
from telegram.ext import CallbackContext


async def start(update: Update, context: CallbackContext) -> None:
    logger.info('get start message')
    if update.message:
        await update.message.reply_text('docker telegram boilerplate')
