from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from DAXXMUSIC import app
from config import OWNER_ID
# vc on
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ")
# vc off
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ**")

# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"{message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} 😉")
           except:
             pass


####

@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)

###
@app.on_message(filters.command("leavegroup")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "sᴜᴄᴄᴇssғᴜʟʟʏ   ʟᴇғᴛ ᴛʜᴇ ɢʀᴏᴜᴘ !!."
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


####

@app.on_message(filters.command("bots"))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"ʙᴏᴛ ʟɪsᴛ - {message.chat.title}\n\n🤖 ʙᴏᴛs\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ @{bot.username}\n\n"
      text3 += f"✅ | *ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ ʙᴏᴛs**: {lenBotList}"  
      await app.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)

