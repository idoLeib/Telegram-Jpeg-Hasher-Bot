import commands
from pytesseract import image_to_string
from PIL import Image


def enter_send_document():
    """
    This function opens the documents list in the Telegram app.

    :return: None
    """
    commands.tap('attach_button')
    commands.tap('attach_file')
    commands.tap('enter_Telegram_files')
    commands.tap('enter_Telegram_documents')


def get_response_msg_using_screenshot():
    """
    This functions gets the bot response in text by taking a screenshot and analysing it.

    :return: the bot's response.
    :rtype: str
    """
    # get screenshot
    command = "adb exec-out screencap -p > response_output.png"
    stdout, stderr = commands.run_adb_command(command)
    image = Image.open('response_output.png')

    # crop and get pic of last msg
    response_msg_height = 450
    width, height = image.size
    crop_box = (0, height - response_msg_height, width, height)
    # Crop the image to the bottom part
    cropped_image = image.crop(crop_box)
    text = image_to_string(cropped_image)

    return text
