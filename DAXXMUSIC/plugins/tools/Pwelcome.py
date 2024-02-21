import os
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from DAXXMUSIC import LOGGER
from DAXXMUSIC import app 
from DAXXMUSIC.zdatabase.Welcomedb import *
import asyncio
from config import LOGGER_ID as LOG_GROUP_ID


COMMAND_HANDLER = ". /".split()


LOGGER = getLogger(__name__)


class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, id, uname):
    background = Image.open("DAXXMUSIC/assets/Welcome.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize(
        (1050, 1050)
    ) 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('DAXXMUSIC/assets/font.ttf', size=120)
    font2 = ImageFont.truetype('DAXXMUSIC/assets/font.ttf', size=90)
    draw.text((2000, 850), f'NAME: {unidecode(user)}', fill=(255, 255, 255), font=font)
    draw.text((1680, 1050), f'ID: {id}', fill=(255, 255, 255), font=font)
    draw.text((1680, 1250), f"USERNAME : {uname}", fill=(255,255,255),font=font)
    pfp_position = (405, 600)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(
        f"downloads/welcome#{id}.png"
    )
    return f"downloads/welcome#{id}.png"


@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one({"chat_id" : chat_id})
    if not A:
       return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "DAXXMUSIC/assets/profilepic.jpg"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption= f"""
**🆆ᴇʟᴄᴏᴍᴇ 🅣ᴏ 🅞ᴜʀ 🅶ʀoᴜᴘ 
║┏━━━━━━➣
║┣⪼ {chat.title} GROUP💫💕
║┣⪼ 𝐍𝐀𝐌𝐄 - {user.mention}
║┣⪼ 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 - {user.username}
║┣⪼ 𝐔𝐒𝐄𝐑_𝐈𝐃 {user.id}
║┗━━━━━━➣
╚═════════════════❍⊱❁۪
╔═════❰𝐑𝐔𝐋𝐄𝐒❱════❍⊱❁۪۪
║
👉 𝐏𝐥𝐞𝐚𝐬𝐞 ❥︎𝐎𝐛𝐞𝐲 ❥︎𝐑𝐮𝐥𝐞𝐬

【💘 𝐍𝐨 𝐏𝐫𝐨𝐌𝐨𝐭𝐢𝐨𝐧】
【🔞 𝐍𝐨 ✰ 𝐀𝐛𝐮𝐬𝐢𝐧𝐠】
【📵 𝐍𝐨 𝐒𝐩𝐚𝐦𝐦𝐢𝐧𝐠】
【👿 𝐍𝐨 ❥︎𝐂𝐡𝐞𝐚𝐭𝐞𝐫𝐬】

💞 𝐓𝐡𝐚𝐧𝐤 𖨆 𝐘𝐨𝐮 𝐅𝐨𝐫 𝐉𝐨𝐢𝐧

🌷 𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 : 𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦𝐬
🌹 𝐓𝐡𝐞𝐧 𝐃𝐌 𝐓𝐨: 
║
╚═════════════════❍⊱❁۪۪
                  🖇🔐🍷
            🌷 𝐅𝐑𝐈𝐄𝐍𝐃𝐒 🌷
        ⇆  ◁ㅤㅤ❚❚ㅤㅤ▷  ↻
•┈┈┈••┈┈┈••••●••••┈┈┈••┈┈┈•
        **
""",
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton (f"TEST", url=f"https://t.me/THE_INDIAN_POLICE")]])
        )
    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass
@app.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message):
    for u in message.new_chat_members:
        if u.id == app.me.id:
            await app.send_message(LOG_GROUP_ID, f"""
**NEW GROUP

NAME: {message.chat.title}
ID: {message.chat.id}
USERNAME: @{message.chat.username}

**
""")


