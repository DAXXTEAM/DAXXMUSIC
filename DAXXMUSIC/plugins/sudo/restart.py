import asyncio
import os
import shutil
import socket
from datetime import datetime
from pyrogram.types import CallbackQuery
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters
import aiohttp
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO
from pyrogram import filters
import config
from DAXXMUSIC import app
from DAXXMUSIC.misc import HAPP, SUDOERS, XCB
from DAXXMUSIC.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from DAXXMUSIC.utils.decorators.language import language
from DAXXMUSIC.utils.pastebin import DAXXBin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

# Modify the existing code...
@app.on_callback_query(filters.regex(r"refresh_logs"))
async def handle_refresh_logs(_, query: CallbackQuery):
    try:
        # Read the content of the log file
        with open("log.txt", "r") as log_file:
            logs_content = log_file.read()

        # Create a new carbon image
        carbon_image = await make_carbon(logs_content)

        # Edit the original message with the new carbon image
        await query.message.edit_photo(carbon_image, caption="**🥀ᴛʜɪs ɪs ɴᴇᴡ ʀᴇғʀᴇsʜᴇᴅ ʟᴏɢs✨**")

    except Exception as e:
        print(f"An error occurred: {e}")

@app.on_message(filters.command(["getlog", "logs", "getlogs"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & SUDOERS)
@language
async def log_(client, message, _):
    try:
        # Read the content of the log file
        with open("log.txt", "r") as log_file:
            logs_content = log_file.read()

        # Create a carbon image
        carbon_image = await make_carbon(logs_content)
        
        # Create an inline keyboard with a refresh button
        refresh_button = InlineKeyboardButton("🥀ʀᴇғʀᴇsʜ✨", callback_data="refresh_logs")
        keyboard = InlineKeyboardMarkup([[refresh_button]])

        # Reply to the message with the carbon image and the inline keyboard
        await message.reply_photo(carbon_image, caption="**🥀ᴛʜɪs ɪs ʏᴏᴜʀ ʟᴏɢs✨**", reply_markup=keyboard)

    except Exception as e:
        print(f"An error occurred: {e}")


@app.on_message(filters.command(["update", "gitpull"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & SUDOERS)
@language
async def update_(client, message, _):
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["server_2"])
    response = await message.reply_text(_["server_3"])
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(_["server_4"])
    except InvalidGitRepositoryError:
        return await response.edit(_["server_5"])
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]
    for checks in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit(_["server_6"])
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: <a href={REPO_}/commit/{info}>{info.summary}</a> ʙʏ -> {info.author}</b>\n\t\t\t\t<b>➥ ᴄᴏᴍᴍɪᴛᴇᴅ ᴏɴ :</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ\n\n<b><u>ᴜᴩᴅᴀᴛᴇs:</u></b>\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await DAXXBin(updates)
        nrs = await response.edit(
            f"<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ\n\n<u><b>ᴜᴩᴅᴀᴛᴇs :</b></u>\n\n<a href={url}>ᴄʜᴇᴄᴋ ᴜᴩᴅᴀᴛᴇs</a>"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    os.system("git stash &> /dev/null && git pull")

    try:
        served_chats = await get_active_chats()
        for x in served_chats:
            try:
                await app.send_message(
                    chat_id=int(x),
                    text=_["server_8"].format(app.mention),
                )
                await remove_active_chat(x)
                await remove_active_video_chat(x)
            except:
                pass
        await response.edit(f"{nrs.text}\n\n{_['server_7']}")
    except:
        pass

    if await is_heroku():
        try:
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            await response.edit(f"{nrs.text}\n\n{_['server_9']}")
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=_["server_10"].format(err),
            )
    else:
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && bash start")
        exit()


@app.on_message(filters.command(["restart"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("ʀᴇsᴛᴀʀᴛɪɴɢ...")
    ac_chats = await get_active_chats()
    for x in ac_chats:
        try:
            await app.send_message(
                chat_id=int(x),
                text=f"{app.mention} ɪs ʀᴇsᴛᴀʀᴛɪɴɢ...\n\nʏᴏᴜ ᴄᴀɴ sᴛᴀʀᴛ ᴩʟᴀʏɪɴɢ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 15-20 sᴇᴄᴏɴᴅs.",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except:
            pass

    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text(
        "» ʀᴇsᴛᴀʀᴛ ᴘʀᴏᴄᴇss sᴛᴀʀᴛᴇᴅ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ sᴇᴄᴏɴᴅs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ sᴛᴀʀᴛs..."
    )
    os.system(f"kill -9 {os.getpid()} && bash start")
