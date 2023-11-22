import os, time
import openai
from pyrogram import filters
from DAXXMUSIC import app
from pyrogram.enums import ChatAction, ParseMode
from gtts import gTTS



openai.api_key = "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"




@app.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(app :app, message):
    
    try:
        start_time = time.time()
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.ask How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            await message.reply_text(f"{x}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        






@app.on_message(filters.command(["assis"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(app :app, message):
    
    try:
        start_time = time.time()
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.assis How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            text = x    
            tts = gTTS(text, lang='en')
            tts.save('output.mp3')
            await app.send_voice(chat_id=message.chat.id, voice='output.mp3')
            os.remove('output.mp3')            
            
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ") 



##### Bing

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
