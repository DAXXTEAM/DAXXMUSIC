import base64
import httpx
import asyncio
from DAXXMUSIC import app
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def create_sticker_set_with_retry(user_id, pack_name, short_name, stickers):
    for attempt in range(3):
        try:
            await bot.invoke(
                pyrogram.raw.functions.stickers.CreateStickerSet(
                    user_id=user_id,
                    title=pack_name,
                    short_name=short_name,
                    stickers=sticks,
                )
            )
            return True
        except pyrogram.errors.FloodWait as e:
            print(f"Retrying after {e.x} seconds due to FloodWait")
            await asyncio.sleep(e.x)
        except pyrogram.errors.RPCError as e:
            print(f"Retrying due to RPCError: {e}")
            await asyncio.sleep(5)

    return False


@app.on_message(filters.command("packkang"))
async def _packkang(app: app, message):
    txt = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ....")
    if not message.reply_to_message:
        await txt.edit('ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ')
        return
    if not message.reply_to_message.sticker:
        await txt.edit('ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ')
        return
    if message.reply_to_message.sticker.is_animated or  message.reply_to_message.sticker.is_video:
        return await txt.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ")
    if len(message.command) < 2:
        pack_name =  f'{message.from_user.first_name}_sticker_pack_by_dil'
    else :
        pack_name = message.text.split(maxsplit=1)[1]
    short_name = message.reply_to_message.sticker.set_name
    stickers = await bot.invoke(
        pyrogram.raw.functions.messages.GetStickerSet(
            stickerset=pyrogram.raw.types.InputStickerSetShortName(
                short_name=short_name),
            hash=0))
    shits = stickers.documents
    sticks = []
    
    for i in shits:
        sex = pyrogram.raw.types.InputDocument(
                id=i.id,
                access_hash=i.access_hash,
                file_reference=i.thumbs[0].bytes
            )
        
        sticks.append(
            pyrogram.raw.types.InputStickerSetItem(
                document=sex,
                emoji=i.attributes[1].alt
            )
        )

    try:
        short_name = f'stikcer_pack_{str(uuid4()).replace("-","")}_by_{bot.me.username}'
        user_id = await bot.resolve_peer(message.from_user.id)
        await bot.invoke(
            pyrogram.raw.functions.stickers.CreateStickerSet(
                user_id=user_id,
                title=pack_name,
                short_name=short_name,
                stickers=sticks,
            )
        )
        await txt.edit(f"Here is your kanged link!\nTotal stickers: {len(sticks)}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Pack Link", url=f"http://t.me/addstickers/{short_name}")]]))
    except Exception as e:
        await message.reply(str(e))
