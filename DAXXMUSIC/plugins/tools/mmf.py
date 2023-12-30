import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from DAXXMUSIC import app
from pyrogram.types import Message
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import base64
import httpx
import requests
import pyrogram
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.raw.types import InputFile
from io import BytesIO
from pyrogram import Client


TEMP_DOWNLOAD_DIRECTORY = []


@app.on_message(filters.command("mmf"))
async def memify(client, message):
    chat_id = message.chat.id
    args = message.text.split(" ", 1)

    if len(args) == 1:
        message.reply_text('Provide some text and reply to image/stickers EXAMPLE: /mmf text')
        return
    xx = await message.reply_text('Memifing your sticker...wait!')

    if message.reply_to_message.sticker.is_animated:
        await xx.edit_text("sorry this function can't work with animated stickers")
        return

    if message.reply_to_message and message.reply_to_message.sticker:
        file_id = message.reply_to_message.sticker.file_id
        with BytesIO() as file:
            file.name = 'mmfsticker.png'
            new_file = await client.get_file(file_id)
            file_content = await new_file.read()
            file.write(file_content)
            file.seek(0)
            img = Image.open(file)

    text = args[1]
    shadowcolor = "black"
    i_width, i_height = img.size
    if os.name == "nt":
        fnt = "./DAXXMUSIC/assets/font2.ttf"
    else:
        fnt = "./DAXXMUSIC/assets/font.ttf"

    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ''
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                      text=u_text, font=m_font, fill=(0, 0, 0))
            draw.text(xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                      text=u_text, font=m_font, fill=(0, 0, 0))
            draw.text(xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                      text=u_text,
                      font=m_font,
                      fill=(0, 0, 0))
            draw.text(xy=(((i_width - u_width) / 2),
                          int(((current_h / 640) * i_width)) + 2),
                      text=u_text,
                      font=m_font,
                      fill=(0, 0, 0))

            draw.text(xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                      text=u_text, font=m_font, fill=(255, 255, 255))
            current_h += u_height + pad
    if lower_text:
        if len(lower_text) > 10:
            current_h -= int((20 / 640) * i_width)  # move text up by 20 pixels
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 2, i_height - u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=(((i_width - u_width) / 2) + 2, i_height - u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=((i_width - u_width) / 2, (i_height - u_height - int((20 / 640) * i_width)) - 2),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=((i_width - u_width) / 2, (i_height - u_height - int((20 / 640) * i_width)) + 2),
                text=l_text, font=m_font, fill=(0, 0, 0))

            draw.text(
                xy=((i_width - u_width) / 2, i_height - u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(255, 255, 255))
            current_h += u_height + pad
    image_name = "memify.webp"
    webp_file = os.path.join(image_name)
    meme = img.save(webp_file, "webp")
    output = open(image_name, "rb")
    await client.send_sticker(chat_id, InputFile(output), reply_to_message_id=message.message_id)
    await xx.delete()

@app.on_message(filters.command("tiny"))
def tinysticker(client, message):
    chat_id = message.chat.id
    im1 = Image.open("DAXXMUSIC/assets/thum.png")

    if message.reply_to_message.sticker.is_animated:
        xx.edit_text("sorry this function can't work with animated stickers")
        return

    if message.reply_to_message and message.reply_to_message.sticker:
        file_id = message.reply_to_message.sticker.file_id
        xx = message.reply_text('Creating your tiny sticker...wait!')

        try:
            with BytesIO() as file:
                file.name = 'tinysticker.png'
                new_file = client.get_file(file_id)
                new_file.download(out=file)
                file.seek(0)
                im = Image.open(file)
            z, d = im.size
            if z == d:
                xxx, yyy = 200, 200
            else:
                t = z + d
                a = z / t
                b = d / t
                aa = (a * 100) - 50
                bb = (b * 100) - 50
                xxx = 200 + 5 * aa
                yyy = 200 + 5 * bb
            k = im.resize((int(xxx), int(yyy)))
            k.save("k.png", format="PNG", optimize=True)
            im2 = Image.open("k.png")
            back_im = im1.copy()
            back_im.paste(im2, (150, 0))
            filename = "y.webp"
            back_im.save(filename, "WEBP", quality=95)
            output = open(filename, "rb")
            client.send_sticker(chat_id, InputFile(output), reply_to_message_id=message.message_id)
            xx.delete()

        except Exception as e:
            message.reply_text(f'Error Report @Sanam_King, {e}')
