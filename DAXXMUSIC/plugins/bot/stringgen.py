from DAXXMUSIC import app
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)


import config


ask_ques = "**» ▷ 𝖢𝐡𝐨𝐨𝐬𝐞 𝖳𝐡𝐞 𝖲𝐭𝐫𝐢𝐧𝐠 𝖶𝐡𝐢𝐜𝐡 𝖸𝐨𝐮 𝖶𝐚𝐧𝐭 ✔️ : :**"
buttons_ques = [
    [
        InlineKeyboardButton("𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬 𝖵2", callback_data="pyrogram"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text=" 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖳𝖱𝖨𝖭𝖦 ", callback_data="generate")
    ]
]




@app. on_message(filters.private & ~filters.forwarded & filters.command(["generate", "geen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, pyrogram =False, old_pyro: bool = False, is_bot: bool = False):
    if pyrogram :
        ty = "𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭"
    else:
        ty = "𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬"
        if not old_pyro:
            ty += " 𝖵2"
    if is_bot:
        ty += " 𝖡𝖮𝖳"
    await msg.reply(f"» 𝖳𝖱𝖸𝖨𝖭𝖦 𝖳𝖮 𝖲𝖳𝖠𝖱𝖳 **{ty}** 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖮𝖱...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝖯𝖫𝖤𝖠𝖲𝖤 𝖲𝖤𝖭𝖣 𝖸𝖮𝖴 **𝖠𝖯𝖨_𝖨𝖣** 𝖳𝖮 𝖯𝖱𝖮𝖢𝖤𝖤𝖣.\n\n𝖢𝖫𝖨𝖢𝖪 𝖮𝖭 /skip 𝖥𝖮𝖱 𝖴𝖲𝖨𝖭𝖦 𝖡𝖮𝖳 𝖠𝖯𝖨.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**𝖠𝖯𝖨_𝖨𝖣** 𝖬𝖴𝖲𝖳 𝖡𝖤 𝖠𝖭 𝖨𝖭𝖳𝖤𝖦𝖤𝖱, 𝖲𝖳𝖠𝖱𝖳 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖨𝖭𝖦 𝖸𝖮𝖴𝖱 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 𝖠𝖦𝖠𝖨𝖭.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "» 𝖭𝖮𝖶 𝖯𝖫𝖤𝖠𝖲𝖤 𝖲𝖤𝖭𝖣 𝖸𝖮𝖴𝖱 **𝖠𝖯𝖨_𝖧𝖠𝖲𝖧** 𝖳𝖮 𝖢𝖮𝖭𝖳𝖨𝖭𝖴𝖤", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "» 𝖯𝖫𝖤𝖠𝖲𝖤 𝖲𝖤𝖭𝖣 𝖸𝖮𝖴 **𝖯𝖧𝖮𝖭𝖤 𝖭𝖴𝖬𝖡𝖤𝖱** 𝖶𝖨𝖳𝖧 𝖢𝖮𝖴𝖭𝖳𝖱𝖸 𝖢𝖮𝖣𝖤𝖥𝖮𝖱 𝖶𝖧𝖨𝖢𝖧 𝖸𝖮𝖴 𝖶𝖠𝖭𝖳 𝖳𝖮 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 \n𝖤𝖷𝖠𝖬𝖯𝖫𝖤 : `+910000000000`'"
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `5432198765:abcdanonymousterabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴀᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if pyrogram  and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif pyrogram :
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await app. connect()
    try:
        code = None
        if not is_bot:
            if pyrogram :
                code = await app. send_code_request(phone_number)
            else:
                code = await app. send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("» ʏᴏᴜʀ **ᴀᴩɪ_ɪᴅ** ᴀɴᴅ **ᴀᴩɪ_ʜᴀsʜ** ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("» ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ **ᴏᴛᴩ** ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪғ ᴏᴛᴩ ɪs `12345`, **ᴩʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if pyrogram :
                await app. sign_in(phone_number, phone_code, password=None)
            else:
                await app. sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ** ᴩᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if pyrogram :
                    await app. sign_in(password=password)
                else:
                    await app. check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if pyrogram :
            await app. start(bot_token=phone_number)
        else:
            await app. sign_in_bot(phone_number)
    if pyrogram :
        string_session = app. session.save()
    else:
        string_session = await app. export_session_string()
    text = f"**𝖳𝐡𝐢𝐬 𝖨𝐬 𝖸𝐨𝐮𝐫 {ty} 𝖲𝐭𝐫𝐢𝐧𝐠 𝖲𝐞𝐬𝐬𝐢𝐨𝐧** \n\n`{string_session}` \n\n**𝖦𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝖡𝐲 :** @TEAMDAXX\n🍒 **𝖭𝖮𝖳𝖤 :** 𝖣𝐨𝐧𝐭 𝖲𝐡𝐚𝐫𝐞 𝖶𝐢𝐭𝐡 𝖠𝐧𝐲𝐨𝐧𝐞 𝖡𝐞𝐜𝐚𝐮𝐬𝐞 𝖧𝐞 𝖢𝐚𝐧 𝖧𝐚𝐜𝐤 𝖸𝐨𝐮𝐫 𝖠𝐥𝐥 𝖣𝐚𝐭𝐚. 🍑 𝖠𝐧𝐝 𝖣𝐨𝐧𝐭 𝖥𝐨𝐫𝐠𝐞𝐭 𝖳𝐨 𝖩𝐨𝐢𝐧 @CYBERDAXX & @CYBERDAXXX 🥺"
    try:
        if not is_bot:
            await app. send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await app.disconnect()
    await bot.send_message(msg.chat.id, "» 𝖲𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝖦𝐫𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝖸𝐨𝐮 {} 𝖲𝐭𝐫𝐢𝐧𝐠 𝖲𝐞𝐬𝐬𝐢𝐨𝐧.\n\n𝖯𝐥𝐞𝐚𝐬𝐞 𝖢𝐡𝐞𝐜𝐤 𝖸𝐨𝐮𝐫 𝖲𝐚𝐯𝐞𝐝 𝖬𝐞𝐬𝐬𝐚𝐠𝐞 𝖳𝐨 𝖦𝐞𝐭 𝖨𝐭 ! \n\n𝖠 𝖲𝐭𝐫𝐢𝐧𝐠  𝖦𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝖡𝐨𝐭 𝖡𝐲 @CYBERDAXXX ♦".format("ᴛᴇʟᴇᴛʜᴏɴ" if pyrogram  else "ᴩʏʀᴏɢʀᴀᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜ !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**» 𝖢𝖠𝖭𝖢𝖤𝖫𝖫𝖤𝖣 𝖳𝖧𝖤 𝖮𝖭𝖦𝖮𝖨𝖭𝖦 𝖲𝖳𝖱𝖨𝖭𝖦 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖨𝖭𝖦 𝖯𝖱𝖮𝖢𝖤𝖲𝖲 !**", quote=True)
        return True
    else:
        return False