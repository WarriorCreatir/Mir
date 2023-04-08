from telegram.ext import ApplicationBuilder

from conf.settings import BOT_TOKEN, logger
from handlers import start_handler


def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(start_handler)

    # Start the Bot
    application.run_polling()
    logger.info('bot started')


if __name__ == '__main__':
    main()
