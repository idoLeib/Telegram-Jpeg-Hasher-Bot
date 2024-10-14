# Telegram Bot: Image Hash Calculator

## Overview
A simple Telegram bot that receives Jpeg/jpg images and sends back their hashes. 

## Features
- Photos: Handles photos sent via Telegram (converted to .jpg).
- Documents: Processes JPEG images sent as documents.
- Hash Calculation: Computes and returns the SHA-256 hash of the image.
- Errors: Sends error messages for every received message that isn't a Jpeg image.

## Requirements
- Python-telegram-bot Pillow
- Telegram bot token
- Docker & Docker Compose
- Telethon
- Pytest

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

## Running the Application

**Using Docker Compose**:
```sh
docker build -t telegram-bot.
docker run -d telegram-bot
```

## Testing
### pytest
Run the tests using `pytest`:
```sh
pytest
```