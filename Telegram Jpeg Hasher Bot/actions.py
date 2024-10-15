import commands
from pytesseract import image_to_string
from PIL import Image


def enter_send_document():
    commands.tap('attach_button')
    commands.tap('attach_file')
    commands.tap('enter_Telegram_files')
    commands.tap('enter_Telegram_documents')


def get_response_msg_using_screenshot():
    # get screenshot
    command = "adb exec-out screencap -p > response_output.png"
    stdout, stderr = commands.run_adb_command(command)
    image = Image.open('response_output.png')

    # crop and get pic of last msg

    width, height = image.size
    crop_box = (0, height - 450, width, height)
    # Crop the image to the bottom part
    cropped_image = image.crop(crop_box)
    text = image_to_string(cropped_image)

    return text
