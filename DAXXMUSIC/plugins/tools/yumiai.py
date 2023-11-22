import requests, config
from pyrogram import filters
from DAXXMUSIC import app
import g4f, random
from pyrogram.enums import ChatAction, ParseMode

api_key ="908fa7e9-220b-4357-ac2f-7eb499005b5f"



@app.on_message(filters.command(["deep" , ],  prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def deepchat(app: app, message):
    name = message.from_user.first_name
    try:
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(f"Hello {name}\nPlease provide text after the /deep command")
        else:
            a = message.text.split(' ', 1)[1]

            data = {
                'text': a,  
            }

            headers = {
                'api-key': api_key,
            }

            r = requests.post("https://api.deepai.org/api/text-generator", data=data, headers=headers)
            response = r.json()
            answer_text = response['output']
            await message.reply_text(f"{answer_text}")
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e}")


#####

@app.on_message(filters.command(["bing"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def bing_ai(app :app, message):
    
    try:
        if len(message.command) < 2:
            await message.reply_text(
            "ʜᴇʟʟᴏ sɪʀ\nᴇxᴀᴍᴘʟᴇ:-.bing How to set girlfriend ?")
        else:
            query = message.text.split(' ', 1)[1]
            response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": query}],  
            provider=g4f.Provider.Bing
            )
            await message.reply_text(f"{response}")     
    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ: {e} ")
