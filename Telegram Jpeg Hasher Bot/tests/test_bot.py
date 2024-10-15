import commands
import actions
import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_telegram():
    """Fixture to start Telegram and enter the bot chat."""
    commands.launch_telegram()
    commands.tap('enter_bot_chat')


def test_send_text():
    """Test to send a text message and check for error in response."""
    commands.send_message("Hello!")
    commands.tap('send_txt')
    commands.wait_for_response()

    response_msg = actions.get_response_msg_using_screenshot()
    assert "Error" in response_msg


def test_send_png():
    """Test to send a PNG file and check for error in response."""
    actions.enter_send_document()
    commands.tap('choose_png_pic')
    commands.tap('send_document')

    commands.wait_for_response()

    response_msg = actions.get_response_msg_using_screenshot()
    assert "Error" in response_msg


def test_send_jpg():
    """Test to send a JPG file and check for success->hash in response."""
    actions.enter_send_document()
    commands.tap('choose_jpg_pic')
    commands.tap('send_document')

    commands.wait_for_response()

    response_msg = actions.get_response_msg_using_screenshot()
    assert "Hash" in response_msg
