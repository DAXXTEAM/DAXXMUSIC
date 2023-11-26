######
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from DAXXMUSIC import app
import config

ask_ques = "» ▷ 𝐂𝐡𝐨𝐨𝐬𝐞 𝐓𝐡𝐞 𝐒𝐭𝐫𝐢𝐧𝐠 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 ✔️ : :"
buttons_ques = [
    [
        InlineKeyboardButton("𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌", callback_data="pyrogram1"),
        InlineKeyboardButton("𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌 𝐕2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("🍷𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍🍷", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌 𝐁𝐎𝐓", callback_data="pyrogram_bot"),
        InlineKeyboardButton("𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐁𝐎𝐓", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text=" 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆 ", callback_data="generate")
    ]
]



@app.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍"
    else:
        ty = "𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌"
        if not old_pyro:
            ty += " 𝐕2"
    if is_bot:
        ty += " 𝐁𝐎𝐓"
    await msg.reply(f"» 𝐓𝐑𝐘𝐈𝐍𝐆 𝐓𝐎 𝐒𝐓𝐀𝐑𝐓 {ty} 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝐏𝐋𝐄𝐀𝐒𝐄 𝐒𝐄𝐍𝐃 𝐘𝐎𝐔 𝐀𝐏𝐈_𝐈𝐃 𝐓𝐎 𝐏𝐑𝐎𝐂𝐄𝐄𝐃.\n\n𝐂𝐋𝐈𝐂𝐊 𝐎𝐍 /skip 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐁𝐎𝐓 𝐀𝐏𝐈.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("𝐀𝐏𝐈_𝐈𝐃 𝐌𝐔𝐒𝐓 𝐁𝐄 𝐀𝐍 𝐈𝐍𝐓𝐄𝐆𝐄𝐑, 𝐒𝐓𝐀𝐑𝐓 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐈𝐍𝐆 𝐘𝐎𝐔𝐑 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 𝐀𝐆𝐀𝐈𝐍.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "» 𝐍𝐎𝐖 𝐏𝐋𝐄𝐀𝐒𝐄 𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐀𝐏𝐈_𝐇𝐀𝐒𝐇 𝐓𝐎 𝐂𝐎𝐍𝐓𝐈𝐍𝐔𝐄", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "» 𝐏𝐋𝐄𝐀𝐒𝐄 𝐒𝐄𝐍𝐃 𝐘𝐎𝐔 𝐏𝐇𝐎𝐍𝐄 𝐍𝐔𝐌𝐁𝐄𝐑 𝐖𝐈𝐓𝐇 𝐂𝐎𝐔𝐍𝐓𝐑𝐘 𝐂𝐎𝐃𝐄𝐅𝐎𝐑 𝐖𝐇𝐈𝐂𝐇 𝐘𝐎𝐔 𝐖𝐀𝐍𝐓 𝐓𝐎 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 \n𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : +910000000000'"
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ʙᴏᴛ_ᴛᴏᴋᴇɴ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : 5432198765:abcdanonymousterabaaplol'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴀᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("» ʏᴏᴜʀ ᴀᴩɪ_ɪᴅ ᴀɴᴅ ᴀᴩɪ_ʜᴀsʜ ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("» ᴛʜᴇ ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ ᴏᴛᴩ ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪғ ᴏᴛᴩ ɪs 12345, ᴩʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs 1 2 3 4 5.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
     
