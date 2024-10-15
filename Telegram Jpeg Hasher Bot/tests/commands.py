import subprocess
import taps
import time


def run_adb_command(command):
    """
    Runs an ADB command and returns the output.

    :return: command output
    :rtype: str
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')


def launch_telegram():
    """Launches the Telegram app on the Android device."""
    command = 'adb shell am start -n org.telegram.messenger/org.telegram.ui.LaunchActivity'
    stdout, stderr = run_adb_command(command)
    time.sleep(2)  # Wait for the app to launch


def send_message(message):
    """Sends a message in the current chat in Telegram."""
    # Simulate text input
    command = f'adb shell input text "{message}"'
    stdout, stderr = run_adb_command(command)
    time.sleep(1)


def tap_coordinates(x, y):
    """Simulates a tap at the specified screen coordinates."""
    command = f'adb shell input tap {x} {y}'
    stdout, stderr = run_adb_command(command)


def tap(action):
    """Tap based on the action name."""
    x, y = taps.taps[action]
    tap_coordinates(x, y)
    time.sleep(1)


def wait_for_response():
    """giving the bot some time to respond"""
    time.sleep(3)



