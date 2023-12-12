from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
from DAXXMUSIC import app

@app.on_message(filters.command("day"))
def date_to_day_command(client: Client, message: Message):
    try:
        # Extract the date from the command message
        command_parts = message.text.split(" ", 1)
        if len(command_parts) == 2:
            input_date = command_parts[1].strip()
            date_object = datetime.strptime(input_date, "%Y-%m-%d")
            day_of_week = date_object.strftime("%A")

            # Reply with the day of the week
            message.reply_text(f"The day of the week for {input_date} is {day_of_week}.")

        else:
            message.reply_text("Please provide a valid date in the format `/day 1947-08-15` ")

    except ValueError as e:
        message.reply_text(f"Error: {str(e)}")
