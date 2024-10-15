# Telegram Bot: Image Hash Calculator

## Overview
A simple Telegram bot that receives Jpeg/jpg images and sends back their hashes. 

## Features
- Accepts `.jpg` or `.jpeg` images and computes their hash.
- Returns an error message for unsupported file formats like `.png`.
- Automated tests using `pytest` and ADB for device interactions.

## Prerequisites

Before setting up the project, make sure you have the following installed:

1. **Python 3.x**: This project is developed with Python.
2. **pip**: Python's package installer to install dependencies.
3. **ADB (Android Debug Bridge)**: Required for testing with Android devices. The `adb.exe` file is included in the project.
4. **Tesseract OCR**: Tesseract is used to extract text from screenshots in tests.
   - [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki)
   
   To verify that Tesseract is installed, run:
   ```bash
   tesseract --version
	```
5. Telegram API Token: Create a bot using Telegram's BotFather and obtain your bot token.


## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/idoLeib/Telegram-Jpeg-Hasher-Bot
    cd Telegram-Jpeg-Hasher-Bot
    ```

2.  **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
3. **Set up the bot configuration**:
	Edit the config.py file with your Telegram bot token. It is reccomended to set the bot token as an environment variable.


## Running the Application

**To run the bot, use the following command:**:
```bash
python bot.py
```

## Testing
### pytest
Run the tests using `pytest`:
```sh
pytest -v test_bot.py
```