import base64
import requests 
import httpx
from DAXXMUSIC import app
from pyrogram import filters

@app.on_message(filters.reply & filters.command("uptest"))
async def upscale_image(client, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ɪᴛ.")
            return

        image = message.reply_to_message.photo.file_id
        file_path = await client.download_media(image)

        with open(file_path, "rb") as image_file:
            f = image_file.read()

        b = base64.b64encode(f).decode("utf-8")

        headers = {"Content-Type": "application/x-www-form-urlencoded"}  # Add headers if required

        async with httpx.AsyncClient() as http_client:
            response = await http_client.post(
                "https://api.picsart.io/tools/1.0/upscale",
                data={"image_data": b},
                headers=headers,
                timeout=30,  # Adjust the timeout as needed
            )

        if response.status_code == 200:
            with open("upscaled_image.png", "wb") as output_file:
                output_file.write(response.content)

            await client.send_document(
                message.chat.id,
                document="upscaled_image.png",
                caption="ʜᴇʀᴇ ɪs ᴛʜᴇ ᴜᴘsᴄᴀʟᴇᴅ ɪᴍᴀɢᴇ!",
            )
        else:
            print(f"Failed to upscale the image. Status Code: {response.status_code}")
            await message.reply_text("Failed to upscale the image. Please try again later.")

    except Exception as e:
        print(f"Failed to upscale the image: {e}")
        await message.reply_text("Failed to upscale the image. Please try again later.")
