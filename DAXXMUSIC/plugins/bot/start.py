import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from DAXXMUSIC import app
from DAXXMUSIC.misc import _boot_
from DAXXMUSIC.plugins.sudo.sudoers import sudoers_list
from DAXXMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from DAXXMUSIC.utils import bot_sys_stats
from DAXXMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from DAXXMUSIC.utils.decorators.language import LanguageStart
from DAXXMUSIC.utils.formatters import get_readable_time
from DAXXMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string



# Random Start Images
YUMI IMG = [
    "https://te.legra.ph/file/5bf629d10afd4af953585.jpg",
    "https://te.legra.ph/file/7a321b99fe99d9d8b5117.jpg",
    "https://te.legra.ph/file/c482a7e55b459ffe07502.jpg",
    "https://telegra.ph//file/0879fbdb307005c1fa8ab.jpg",
    "https://telegra.ph//file/19e3a9d5c0985702497fb.jpg",
    "https://telegra.ph//file/b5fa277081dddbddd0b12.jpg",
    "https://telegra.ph//file/96e96245fe1afb82d0398.jpg",
    "https://telegra.ph//file/fb140807129a3ccb60164.jpg",
    "https://telegra.ph//file/09c9ea0e2660efae6f62a.jpg",
    "https://telegra.ph//file/3b59b15e1914b4fa18b71.jpg",
    "https://telegra.ph//file/efb26cc17eef6fe82d910.jpg",
    "https://telegra.ph//file/ab4925a050e07b00f63c5.jpg",
    "https://telegra.ph//file/d169a77fd52b46e421414.jpg",
    "https://telegra.ph//file/dab9fc41f214f9cded1bb.jpg",
    "https://telegra.ph//file/e05d6e4faff7497c5ae56.jpg",
    "https://telegra.ph//file/1e54f0fff666dd53da66f.jpg",
    "https://telegra.ph//file/18e98c60b253d4d926f5f.jpg",
    "https://telegra.ph//file/b1f7d9702f8ea590b2e0c.jpg",
    "https://telegra.ph//file/7bb62c8a0f399f6ee1f33.jpg",
    "https://telegra.ph//file/dd00c759805082830b6b6.jpg",
    "https://telegra.ph//file/3b996e3241cf93d102adc.jpg",
    "https://telegra.ph//file/610cc4522c7d0f69e1eb8.jpg",
    "https://telegra.ph//file/bc97b1e9bbe6d6db36984.jpg",
    "https://telegra.ph//file/2ddf3521636d4b17df6dd.jpg",
    "https://telegra.ph//file/72e4414f618111ea90a57.jpg",
    "https://telegra.ph//file/a958417dcd966d341bfe2.jpg",
    "https://telegra.ph//file/0afd9c2f70c6328a1e53a.jpg",
    "https://telegra.ph//file/82ff887aad046c3bcc9a3.jpg",
    "https://telegra.ph//file/8ba64d5506c23acb67ff4.jpg",
    "https://telegra.ph//file/8ba64d5506c23acb67ff4.jpg",
    "https://telegra.ph//file/a7cba6e78bb63e1b4aefb.jpg",
    "https://telegra.ph//file/f8ba75bdbb9931cbc8229.jpg",
    "https://telegra.ph//file/07bb5f805178ec24871d3.jpg",
    "https://telegra.ph/file/ec0ed654f5f5cefc90f95.jpg",
    "https://telegra.ph/file/f6aa2a3659462401cb600.jpg",
    "https://telegra.ph/file/0c3d91bcf75524a844883.jpg",
    "https://telegra.ph/file/6c5df27e71e074f1c7123.jpg",
    "https://telegra.ph/file/ff2ddc282fe7868e3cf73.jpg",
    "https://telegra.ph/file/6130ea9373d5f60898a52.jpg",
    "https://telegra.ph/file/45e5da1eab8f5892981ca.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]




@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(YUMI_PICS),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await message.reply_photo(
            random.choice(YUMI_PICS),
            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM,served_users,served_chats),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(YUMI_PICS),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(YUMI_PICS),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
