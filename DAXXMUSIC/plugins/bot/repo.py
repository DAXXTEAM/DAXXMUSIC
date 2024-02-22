from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """
╔════════════════❍⊱❁۪۪
║┏━━━━━━➣
║┣⪼ 𝗕𝗘𝗦𝗧 𝗠𝗨𝗦𝗜𝗖 𝗣𝗟𝗔𝗬𝗘𝗥 🌹
║┣⪼ 𝗕𝗘𝗦𝗧 𝗩𝗣𝗦 𝗦𝗘𝗥𝗩𝗘𝗥 🥀
║┗━━━━━━➣       
╭──• ❰ 𝗔𝗟𝗟 𝗕𝗢𝗧❱ •──────➤ 
┣ ▫️ @BARISH_MUSIC_BOT
┣ ▫️ @LOVER_X_MUSIC_BOT
┣ ▫️ @MERA_X_PYAR_BOT
╰─────── • ◆ • ───────➤
║
║╔═════ஜ۩۞۩ஜ══════╗
║ 𝗗𝗠 @PAWAN_IS_BACK
║╚═════ஜ۩۞۩ஜ══════╝ ╚═════════════════❍⊱❁
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ➕ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("🚀ʜᴇʟᴘ🚀", url="https://t.me/angel_world11"),
          InlineKeyboardButton("🍃ᴏᴡɴᴇʀ🍃", url="https://t.me/PAWAN_IS_BACK"),
          ],
               [
                InlineKeyboardButton("ᴀɴɢᴇʟ🦋ᴇᴅɪᴛx", url=f"https://t.me/mr_editx"),

],
[
InlineKeyboardButton("ᴏғғɪᴄɪᴀʟ🦋ɢʀᴏᴜᴘ", url=f"https://t.me/angel_world11"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/03105716906ef6cbcd98e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
