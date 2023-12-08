from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DAXXMUSIC import app

# Dictionary to store buttons created by users
user_buttons = {}

@app.on_message(filters.command("button") & filters.private)
async def create_button(_, message):
    try:
        # Check if the command has the required parameters
        command_parts = message.text.split(" ", 1)
        if len(command_parts) == 2:
            button_data = command_parts[1].split()
            
            # Ensure an even number of arguments (text and URL pairs)
            if len(button_data) % 2 == 0:
                # Create a list of InlineKeyboardButtons based on the pairs
                buttons = [
                    InlineKeyboardButton(button_data[i], url=button_data[i + 1])
                    for i in range(0, len(button_data), 2)
                ]
                
                # Create an inline keyboard with the specified buttons
                keyboard = InlineKeyboardMarkup([buttons])
                
                # Send the message with the buttons
                sent_message = await message.reply_text("𝗕𝗨𝗧𝗧𝗢𝗡 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 𝗗𝗢𝗡𝗘✅", reply_markup=keyboard)
                
                # Store the button information for future reference
                user_buttons[message.from_user.id] = {'message_id': sent_message.message_id, 'buttons': buttons}
            else:
                await message.reply("Invalid number of arguments. Use /button Text1 URL1 Text2 URL2 ...")
        else:
            await message.reply("Invalid command format. Use /button Text1 URL1 Text2 URL2 ...")
    except Exception as e:
        print(f"Error: {e}")

@app.on_callback_query()
async def handle_button_click(_, callback_query):
    try:
        # Extract user ID from the callback data
        user_id = callback_query.from_user.id
        
        # Get the stored button information
        button_info = user_buttons.get(user_id)
        
        if button_info:
            # Find the clicked button
            clicked_button = next(button for button in button_info['buttons'] if button.callback_data == callback_query.data)
            
            # Edit the original message with the clicked button's URL
            await callback_query.edit_message_text(f"Click the button below:\nURL: {clicked_button.url}")
    except Exception as e:
        print(f"Error: {e}")
