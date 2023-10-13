import asyncio, os, time, aiohttp
from pathlib import Path
from blackpink import blackpink as bp
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from DAXXMUSIC import DAXX
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram.types import *
from typing import Union, Optional


button = InlineKeyboardMarkup([[
            InlineKeyboardButton("⌯ ᴄʟᴏsᴇ ⌯", callback_data="close_data")
                              ]])

# --------------------------------------------------------------------------------- #


get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #


async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],    
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )


    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path
   

# --------------------------------------------------------------------------------- #

bg_path = "./DAXXMUSIC/Helper/resources/userinfo.png"
font_path = "./DAXXMUSIC/Helper/resources/DAXXMUSIC.ttf"

# --------------------------------------------------------------------------------- #


INFO_TEXT = """
**ᴜsᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ**:

**ᴜsᴇʀ ɪᴅ:** `{}`

**ɴᴀᴍᴇ:** {}
**ᴜsᴇʀɴᴀᴍᴇ: @{}
**ᴍᴇɴᴛɪᴏɴ:** {}

**ᴜsᴇʀ sᴛᴀᴛᴜs:**\n`{}`\n
**ᴅᴄ ɪᴅ:** {}
**ʙɪᴏ:** {}
"""

# --------------------------------------------------------------------------------- #

async def userstatus(user_id):
   try:
      user = await DAXXMUSIC.get_users(user_id)
      x = user.status
      if x == enums.UserStatus.RECENTLY:
         return "User was seen recently."
      elif x == enums.UserStatus.LAST_WEEK:
          return "User was seen last week."
      elif x == enums.UserStatus.LONG_AGO:
          return "User was seen long ago."
      elif x == enums.UserStatus.OFFLINE:
          return "User is offline."
      elif x == enums.UserStatus.ONLINE:
         return "User is online."
   except:
        return "**sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ !**"
    

# --------------------------------------------------------------------------------- #

@DAXXMUSIC.on_message(filters.command(["info", "userinfo"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if not message.reply_to_message and len(message.command) == 2:
        try:
            user_id = message.text.split(None, 1)[1]
            user_info = await DAXXMUSIC.get_chat(user_id)
            user = await DAXXMUSIC.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await DAXXMUSIC.download_media(user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await DAXXMUSIC.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=button)
        except Exception as e:
            await message.reply_text(str(e))        
      
    elif not message.reply_to_message:
        try:
            user_info = await DAXXMUSIC.get_chat(user_id)
            user = await DAXXMUSIC.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await DAXXMUSIC.download_media(user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await DAXXMUSIC.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=button)
        except Exception as e:
            await message.reply_text(str(e))

            
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        try:
            user_info = await DAXXMUSIC.get_chat(user_id)
            user = await DAXXMUSIC.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await DAXXMUSIC.download_media(message.reply_to_message.from_user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await DAXXMUSIC.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=button)
        except Exception as e:
            await message.reply_text(str(e))


# --------------------------------------------------------------------------------- #

@DAXXMUSIC.on_message(filters.command('id'))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇssᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
import asyncio, os, time, aiohttp
from pathlib import Path
from blackpink import blackpink as bp
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from DAXXMUSIC import DAXX
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram.types import *
from typing import Union, Optional


button = InlineKeyboardMarkup([[
            InlineKeyboardButton("⌯ ᴄʟᴏsᴇ ⌯", callback_data="close_data")
                              ]])

# --------------------------------------------------------------------------------- #


get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #


async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],    
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )


    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path
   

# --------------------------------------------------------------------------------- #

bg_path = "./DAXXMUSIC/Helper/resources/userinfo.png"
font_path = "./DAXXMUSIC/Helper/resources/DAXXMUSIC.ttf"

# --------------------------------------------------------------------------------- #


INFO_TEXT = """
**ᴜsᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ**:

**ᴜsᴇʀ ɪᴅ:** `{}`

**ɴᴀᴍᴇ:** {}
**ᴜsᴇʀɴᴀᴍᴇ: @{}
**ᴍᴇɴᴛɪᴏɴ:** {}

**ᴜsᴇʀ sᴛᴀᴛᴜs:**\n`{}`\n
**ᴅᴄ ɪᴅ:** {}
**ʙɪᴏ:** {}
"""

# --------------------------------------------------------------------------------- #

async def userstatus(user_id):
   try:
      user = await DAXXMUSIC.get_users(user_id)
      x = user.status
      if x == enums.UserStatus.RECENTLY:
         return "User was seen recently."
      elif x == enums.UserStatus.LAST_WEEK:
          return "User was seen last week."
      elif x == enums.UserStatus.LONG_AGO:
          return "User was seen long ago."
      elif x == enums.UserStatus.OFFLINE:
          return "User is offline."
      elif x == enums.UserStatus.ONLINE:
         return "User is online."
   except:
        return "**sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ !**"
    

# --------------------------------------------------------------------------------- #

@DAXXMUSIC.on_message(filters.command(["info", "userinfo"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if not message.reply_to_message and len(message.command) == 2:
        try:
            user_id = message.text.split(None, 1)[1]
            user_info = await DAXXMUSIC.get_chat(user_id)
            user = await DAXXMUSIC.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await DAXXMUSIC.download_media(user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await DAXXMUSIC.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=button)
        except Exception as e:
            await message.reply_text(str(e))        
      
    elif not message.reply_to_message:
        try:
            user_info = await DAXXMUSIC.get_chat(user_id)
            user = await DAXXMUSIC.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await DAXXMUSIC.download_media(user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await DAXXMUSIC.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=button)
        except Exception as e:
            await message.reply_text(str(e))

            
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        try:
            user_info = await DAXXMUSIC.get_chat(user_id)
            user = await DAXXMUSIC.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await DAXXMUSIC.download_media(message.reply_to_message.from_user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await DAXXMUSIC.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=button)
        except Exception as e:
            await message.reply_text(str(e))


# --------------------------------------------------------------------------------- #

@DAXXMUSIC.on_message(filters.command('id'))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇssᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )


# --------------------------------------------------------------------------------- #

@DAXXMUSIC.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("ᴄʜᴇᴄᴋ ɢɪᴛʜᴜʙ ᴘʀᴏғɪʟᴇ ᴜsᴀɢᴇ : /github Sumit0045")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}**

**ᴜsᴇʀɴᴀᴍᴇ :** `{username}`
**ʙɪᴏ :** `{bio}`
**ʟɪɴᴋ :** [Here]({url})
**ᴄᴏᴍᴩᴀɴʏ :** `{company}`
**ᴄʀᴇᴀᴛᴇᴅ ᴏɴ :** `{created_at}`
**ʀᴇᴩᴏsɪᴛᴏʀɪᴇs :** `{repositories}`
**ʙʟᴏɢ :** `{blog}`
**ʟᴏᴄᴀᴛɪᴏɴ :** `{location}`
**ғᴏʟʟᴏᴡᴇʀs :** `{followers}`
**ғᴏʟʟᴏᴡɪɴɢ :** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=button)



# --------------------------------------------------------------------------------- #


@DAXXMUSIC.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"**ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs** : {result}"
    except:
        response = "**ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ**"
    message.reply(response)


# ------------------------------------------------------------------------------- #


@DAXXMUSIC.on_message(filters.command("blackpink"))
async def blackpink(_, message):
    text = message.text[len("/blackpink ") :]
    bp(f"{text}").save(f"blackpink_{message.from_user.id}.png")
    await message.reply_photo(f"blackpink_{message.from_user.id}.png", reply_markup=button)
    os.remove(f"blackpink_{message.from_user.id}.png")






 parse_mode=ParseMode.DEFAULT,
    )


# --------------------------------------------------------------------------------- #

@DAXXMUSIC.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("ᴄʜᴇᴄᴋ ɢɪᴛʜᴜʙ ᴘʀᴏғɪʟᴇ ᴜsᴀɢᴇ : /github Sumit0045")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
          blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}**

**ᴜsᴇʀɴᴀᴍᴇ :** `{username}`
**ʙɪᴏ :** `{bio}`
**ʟɪɴᴋ :** [Here]({url})
**ᴄᴏᴍᴩᴀɴʏ :** `{company}`
**ᴄʀᴇᴀᴛᴇᴅ ᴏɴ :** `{created_at}`
**ʀᴇᴩᴏsɪᴛᴏʀɪᴇs :** `{repositories}`
**ʙʟᴏɢ :** `{blog}`
**ʟᴏᴄᴀᴛɪᴏɴ :** `{location}`
**ғᴏʟʟᴏᴡᴇʀs :** `{followers}`
**ғᴏʟʟᴏᴡɪɴɢ :** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=button)



# --------------------------------------------------------------------------------- #

