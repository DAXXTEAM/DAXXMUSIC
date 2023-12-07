import pyrogram
import time
from pyrogram import filters
from pyrogram import Client
from DAXXMUSIC import app
from DAXXMUSIC.misc import SUDOERS

# Define the command handler
@app.on_message(filters.command("raid", prefixes=".")  & SUDOERS)
def repeat_message(client, message):
    # Get the text following the .raid command
    command_args = message.text.split(".raid", 1)[-1].strip()

    # Check if the user provided a number of times to repeat (e.g., .raid 5 Hello)
    try:
        num_times, text_to_repeat = command_args.split(maxsplit=1)
        num_times = int(num_times)
    except ValueError:
        # If not, default to repeating 1 time
        num_times = 1
        text_to_repeat = command_args

    for _ in range(num_times):
        # Send the repeated message to the Telegram chat
        message.reply_text(text_to_repeat)
        time.sleep(1)  # Wa
