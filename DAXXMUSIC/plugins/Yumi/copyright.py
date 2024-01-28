from pyrogram import Client, filters
from DAXXMUSIC import app
from pyrogram.types import Message




@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_long_messages(client, message):
    try:
        if len(message.text.split()) >= 10:

       
            print(f"Deleted message from {message.from_user.username}: {message.text}")
            
            
            await message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")
        
