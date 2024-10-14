import os


class Config(object):
    """
    Configuration class for storing environment variables.
    Attributes:
        TELEGRAM_BOT_TOKEN (str): The token used to authenticate the bot with Telegram's API.
    """
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
