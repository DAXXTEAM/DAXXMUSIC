import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DAXXMUSIC import app
from DAXXMUSIC.core.userbot import assistants
from config import OWNER_ID

BOT_LIST = ["VCLUBHELP_BOT", "ClawdR0Bot", "MUSICXBOT", "VclubTechxBot"]


def _get_assistant():
    for uid, client in assistants.items():
        return client
    return None


@app.on_message(filters.command("botschk") & filters.user(OWNER_ID))
async def bots_chk(_, message):
    ubot = _get_assistant()
    if not ubot:
        return await message.reply_text("❌ **ɴᴏ ᴀssɪsᴛᴀɴᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ!**")

    msg = await message.reply_photo(
        photo="https://telegra.ph/file/4d303296e4fac9a40ea07.jpg",
        caption="**ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛs sᴛᴀᴛs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ...**"
    )
    
    response = "**⚡ ʙᴏᴛs sᴛᴀᴛᴜs ᴄʜᴇᴄᴋ ⚡**\n\n"
    alive = 0
    dead = 0

    for bot_username in BOT_LIST:
        try:
            bot = await app.get_users(bot_username)
            # Send /start from assistant (userbot)
            await ubot.send_message(bot.id, "/start")
            await asyncio.sleep(3)
            
            # Check if bot replied
            is_alive = False
            async for bot_message in ubot.get_chat_history(bot.id, limit=1):
                if bot_message.from_user and bot_message.from_user.id == bot.id:
                    is_alive = True
            
            if is_alive:
                response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✅**\n\n"
                alive += 1
            else:
                response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❌**\n\n"
                dead += 1
        except Exception as e:
            response += f"╭⎋ @{bot_username}\n╰⊚ **sᴛᴀᴛᴜs: ᴇʀʀᴏʀ ⚠️** __{str(e)[:30]}__\n\n"
            dead += 1

    response += f"━━━━━━━━━━━━━━━\n**✅ ᴏɴʟɪɴᴇ: {alive} | ❌ ᴏғғʟɪɴᴇ: {dead}**"

    await msg.edit_caption(response)
