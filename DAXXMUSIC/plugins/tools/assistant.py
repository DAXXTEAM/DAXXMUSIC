from DAXXMUSIC.core.userbot import assistants
from DAXXMUSIC import userbot as us, app

def _get_ubot():
    """Safely get assistant client"""
    if 1 in assistants:
        return us.one
    elif 2 in assistants:
        return us.two
    return None
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC.misc import SUDOERS
from config import BANNED_USERS, OWNER_ID


@app.on_message(filters.command(["asspfp", "setpfp"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("𝙉𝙤 𝘾𝙝𝙖𝙣𝙜𝙞𝙣𝙜 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘...")
        img = await message.reply_to_message.download()
        ubot = _get_ubot()
        if not ubot:
            return await message.reply_text("Assistant not connected!")
        try:
            await ubot.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» {ubot.me.mention} 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮.."
            )
        except:
            return await fuk.edit_text("𝙁𝙖𝙞𝙡𝙚𝙙 𝙩𝙤 𝘾𝙝𝙖𝙣𝙜𝙚 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘.")
    else:
        await message.reply_text(
            "𝙍𝙚𝙥𝙡𝙮 𝙏𝙤 𝘼 𝙋𝙝𝙤𝙩𝙤 𝙁𝙤𝙧 𝘾𝙝𝙖𝙣𝙜𝙞𝙣𝙜 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘.."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
    try:
        ubot = _get_ubot()
        if not ubot:
            return await message.reply_text("Assistant not connected!")
        pfp = [p async for p in ubot.get_chat_photos("me")]
        await ubot.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text( "𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘." )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("𝙁𝙖𝙞𝙡𝙚𝙙 𝙏𝙤 𝘿𝙚𝙡𝙚𝙩𝙚 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘.")


@app.on_message(filters.command(["assbio", "setbio"]) & filters.user(OWNER_ID))
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            ubot = _get_ubot()
        if not ubot:
            return await message.reply_text("Assistant not connected!")
            await ubot.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ubot.me.mention} 𝘽𝙞𝙤 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        ubot = _get_ubot()
        if not ubot:
            return await message.reply_text("Assistant not connected!")
        await ubot.update_profile(bio=newbio)
        return await message.reply_text(f"» {ubot.me.mention} 𝘽𝙞𝙤 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮.")
    else:
        return await message.reply_text(
            "𝙍𝙚𝙥𝙡𝙮 𝙏𝙤 𝘼 𝙈𝙖𝙨𝙨𝙖𝙜𝙚 𝙊𝙧 𝙂𝙞𝙫𝙚 𝙎𝙤𝙢𝙚 𝙏𝙚𝙭𝙩 𝙏𝙤 𝙎𝙚𝙩 𝙄𝙩 𝘼𝙨 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝘽𝙞𝙤."
        )


@app.on_message(filters.command(["assname", "setname"]) & filters.user(OWNER_ID))
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            ubot = _get_ubot()
        if not ubot:
            return await message.reply_text("Assistant not connected!")
            await ubot.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ubot.me.mention} 𝙉𝙖𝙢𝙚 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        ubot = _get_ubot()
        if not ubot:
            return await message.reply_text("Assistant not connected!")
        await ubot.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ubot.me.mention} 𝙉𝙖𝙢𝙚 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮.")
    else:
        return await message.reply_text(
            "𝙍𝙚𝙥𝙡𝙮 𝙩𝙤 𝙖 𝙈𝙖𝙨𝙨𝙖𝙜𝙚 𝙤𝙧 𝙂𝙞𝙫𝙚 𝙎𝙤𝙢𝙚 𝙏𝙚𝙭𝙩 𝙏𝙤 𝙎𝙚𝙩 𝙄𝙩 𝘼𝙨 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙉𝙚𝙬 𝙉𝙖𝙢𝙚"
        )
