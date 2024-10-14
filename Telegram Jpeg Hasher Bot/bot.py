from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import handler
from config import Config


async def start(update: Update, context):
    """
    Sends a welcome message when the /start command is issued.

    This function is triggered when a user sends the /start command to the bot.
    It responds with a message prompting the user to send a .jpg/.jpeg image to calculate its hash.

    :param update: (telegram.Update): Contains information about the incoming update (message, user info, etc.).
    :param context: (telegram.ext.CallbackContext): Provides context information about the ongoing conversation.

    :return: None
    """
    await update.message.reply_text("Welcome! Send me a .jpg/.jpeg image to calculate its hash.")


def main():
    """
    Initializes and runs the Telegram bot.

    This function sets up the Telegram bot to respond to Jpeg images with their hashes,
    and error messages to anything else.

    Raises:
        ValueError: If the TELEGRAM_BOT_TOKEN is not found in the `Config` class.

    :return: None
    """
    token = Config.TELEGRAM_BOT_TOKEN

    # Ensure the token is available
    if not token:
        raise ValueError("No TELEGRAM_BOT_TOKEN found. Please set the environment variable.")

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    
    # checking if the photo is in Jpeg/Jpg format
    application.add_handler(MessageHandler(filters.PHOTO, handler.check_image))
    # checking if the document is a photo in Jpeg/Jpg format
    application.add_handler(MessageHandler(filters.Document.ALL, handler.check_document))
    # sending error message to all other types of input
    application.add_handler(MessageHandler(~filters.PHOTO & ~filters.Document.ALL, handler.handle_non_photo))
    
    application.run_polling()


if __name__ == '__main__':
    main()
