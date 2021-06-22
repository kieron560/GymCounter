import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from scrapper import get_info
import os

PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1726981118:AAHqAMtbZdZRLwTdo1DED0LDD6h8PUBvNNw'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Yall better not be doing just bench presses okay')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Enter /gym to get the timing for Elias')

def elias (update, context):
     update.message.reply_text(gym(1))

def ehub (update, context):
     update.message.reply_text(gym(2))

def gym(choice):
    result = get_info(choice)
    return (
        "Location: " + result[0] + "\n" +
        "Updated at: " + result[1] + "\n" +
        "Current: " + result[2] + "\n" +
        "Waiting: " + result[3] + "\n" +
        "\n" + "Train hard bitches!"
    )

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("elias", elias))
    dp.add_handler(CommandHandler("ehub", ehub))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://protected-beach-15254.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()


