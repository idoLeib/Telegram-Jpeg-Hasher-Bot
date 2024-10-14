from image_processing import send_image_hash


async def check_image(update, context):
    """
    Handles images sent as photos. Ensures the file is in .jpg/.jpeg format and calculates its hash.
    Sends an error message if the file is not in the correct format.
    
    :param update: (telegram.Update): Contains information about the incoming update (message, user info, etc.).
    :param context: (telegram.ext.CallbackContext): Provides context information about the ongoing conversation.

    :return: None
    """
    file_info = await update.message.photo[-1].get_file()

    # Check the file extension to ensure it's JPEG/JPG
    if not file_info.file_path.endswith(('jpg', 'jpeg')):
        await update.message.reply_text("Error: None acceptable image format. Only .jpg/.jpeg files are allowed.")
        return
    # valid image- continue to send hash
    await send_image_hash(update, context, file_info)


async def check_document(update, context):
    """
    Handles images sent as documents. Ensures the file is in .jpg/.jpeg format based on file extension and MIME type.
    Sends an error message if the file is not in the correct format.

    :param update: (telegram.Update): Contains information about the incoming update (message, user info, etc.).
    :param context: (telegram.ext.CallbackContext): Provides context information about the ongoing conversation.

    :return: None
    """
    file_info = update.message.document

    # Check the file extension and mime to ensure it's JPEG/JPG
    if not file_info.file_name.endswith(('jpg', 'jpeg')) or file_info.mime_type != 'image/jpeg':
        await update.message.reply_text("Error: Only .jpg/.jpeg files are allowed.")
        return

    # valid image- continue to send hash
    await send_image_hash(update, context, await file_info.get_file())


async def handle_non_photo(update, context):
    """
    Sends an error message for any input that is not a valid image (neither a photo nor a document).

    :param update: (telegram.Update): Contains information about the incoming update (message, user info, etc.).
    :param context: (telegram.ext.CallbackContext): Provides context information about the ongoing conversation.

    :return: None
    """
    await update.message.reply_text("Error: Not an image. Only .jpg/.jpeg files are accepted.")

