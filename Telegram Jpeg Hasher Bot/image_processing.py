import hashlib


async def send_image_hash(update, context, file):
    """
    Sends the SHA-256 hash of the image to the user. Handles errors if any occur during hash calculation.
    
    :param update: (telegram.Update): Contains information about the incoming update (message, user info, etc.).
    :param context: (telegram.ext.CallbackContext): Provides context information about the ongoing conversation.
    :param file: (telegram._files.file.File) the image as a telegram file to download and hash.
    
    :return: None
    """
    try:
        img_hash = await calculate_image_hash(file)
        await update.message.reply_text(f"Hash: {img_hash}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def calculate_image_hash(file):
    """
    Calculates the SHA-256 hash of the image file.
    
    :param file: (telegram._files.file.File) the image as a telegram file to download and hash.
    :return: None
    """
    file_bytes = await file.download_as_bytearray()

    # Calculate and return the SHA-256 hash of the image
    img_hash = hashlib.sha256(file_bytes).hexdigest()
    return img_hash
