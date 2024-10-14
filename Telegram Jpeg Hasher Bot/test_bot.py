import pytesseract


import subprocess
import time
from pytesseract import image_to_string
from PIL import Image

def run_adb_command(command):
    """Runs an ADB command and returns the output."""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

def launch_telegram():
    """Launches the Telegram app on the Android device."""
    command = 'adb shell am start -n org.telegram.messenger/org.telegram.ui.LaunchActivity'
    stdout, stderr = run_adb_command(command)
    print("Launching Telegram:", stdout, stderr)

def send_message(message):
    """Sends a message in the current chat in Telegram."""
    # Simulate text input
    command = f'adb shell input text "{message}"'
    stdout, stderr = run_adb_command(command)
    print("Sending message:", stdout, stderr)


def tap_coordinates(x, y):
    """Simulates a tap at the specified screen coordinates."""
    command = f'adb shell input tap {x} {y}'
    stdout, stderr = run_adb_command(command)
    print(f"Tapping at ({x}, {y}):", stdout, stderr)


def start():
    launch_telegram()
    time.sleep(2)  # Wait for the app to launch

    # Tap to open the correct bot
    tap_coordinates(200, 400)  # Adjust coordinates to the bot location
    time.sleep(2)  # Wait for the bot's chat to open


def get_response_msg_using_screenshot():
    #get screenshot
    command = "adb exec-out screencap -p > text_output.png"
    stdout, stderr = run_adb_command(command)
    image = Image.open('text_output.png')

    #crop and get pic of last msg

    width, height = image.size
    crop_box = (0, height - 450, width, height)
    # Crop the image to the bottom part
    cropped_image = image.crop(crop_box)
    text = image_to_string(cropped_image)

    return text


def test_text():
    send_message("Hello!")
    time.sleep(2)
    tap_coordinates(1000, 2100)#send
    time.sleep(3)#wait for response

    response_msg = get_response_msg_using_screenshot()
    print(response_msg)
    print("Error" in response_msg)
    assert "Error" in response_msg


def main():
    start()
    test_text()


    # Add more actions or validations as needed

if __name__ == "__main__":
    main()
