from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import aiohttp
import re
import os
from DAXXMUSIC import app


@app.on_message(filters.command("tg"))
async def search_command(_, message):
    msg = await message.reply("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(
            f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={message.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}",
            headers={"x-referer": "https://explorer.apis.google.com"},
        ) as r:
            response = await r.json()
            result = ""

            if not response.get("items"):
                return await msg.edit("No results found!")

            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r"\/\d", item["link"]):
                    link = re.sub(r"\/\d", "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"

            prev_and_next_btns = [
                [InlineKeyboardButton("▶️Next▶️", callback_data=f"next {start+10} {message.text.split()[1]}")]
            ]
            await msg.edit(result, reply_markup=InlineKeyboardMarkup(prev_and_next_btns), disable_web_page_preview=True)
            await session.close()


@app.on_callback_query(filters.regex(r"prev (.*) (.*)"))
async def prev_callback(_, callback_query):
    start = int(callback_query.data.split()[1])
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={(callback_query.data.split()[2]).encode('utf-8')}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}",
            headers={"x-referer": "https://explorer.apis.google.com"},
        ) as r:
            response = await r.json()
            if response.get("error"):
                return await callback_query.answer("No more results!")

            result = ""
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r"\/\d", item["link"]):
                    link = re.sub(r"\/\d", "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"

            prev_and_next_btns = [
                [InlineKeyboardButton("◀️Prev◀️", callback_data=f"prev {start-10} {(callback_query.data.split()[2]).decode('utf-8')}"),
                 InlineKeyboardButton("▶️Next▶️", callback_data=f"next {start+10} {(callback_query.data.split()[2]).decode('utf-8')}")]
            ]
            await callback_query.edit_message_text(result, reply_markup=InlineKeyboardMarkup(prev_and_next_btns), disable_web_page_preview=True)
            await session.close()


@app.on_callback_query(filters.regex(r"next (.*) (.*)"))
async def next_callback(_, callback_query):
    start = int(callback_query.data.split()[1])
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={(callback_query.data.split()[2]).encode('utf-8')}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}",
            headers={"x-referer": "https://explorer.apis.google.com"},
        ) as r:
            response = await r.json()
            if response["searchInformation"]["totalResults"] == "0":
                return await callback_query.answer("No more results!")

            result = ""
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r"\/\d", item["link"]):
                    link = re.sub(r"\/\d", "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"

            prev_and_next_btns = [
                [InlineKeyboardButton("◀️Prev◀️", callback_data=f"prev {start-10} {(callback_query.data.split()[2]).decode('utf-8')}"),
                 InlineKeyboardButton("▶️Next▶️", callback_data=f"next {start+10} {(callback_query.data.split()[2]).decode('utf-8')}")]
            ]
            await callback_query.edit_message_text(result, reply_markup=InlineKeyboardMarkup(prev_and_next_btns), disable_web_page_preview=True)
            await session.close()
