from pyrogram import Client, filters
from pornhub_api import PornhubApi
from pornhub_api.backends.aiohttp import AioHttpBackend
from DAXXMUSIC import app

# Initialize the Pornhub API
pornhub_api = PornhubApi(backend=AioHttpBackend())

# Command to search and send an adult video based on the title
@app.on_message(filters.command("porn"))
async def give_video(_, message):
    try:
        # Extract the title from the command
        title = " ".join(message.command[1:])

        if not title:
            await message.reply_text("Please enter a title for the video.")
            return

        # Search for a video on Pornhub API based on the title
        src = await pornhub_api.search.search(title)

        if src.videos:
            video = src.videos[0]
            # Send the video details to the user
            await message.reply_text(f"Title: {video.title}\nURL: {video.url}")
        else:
            await message.reply_text("No matching video found.")

    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
