import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from DAXXMUSIC import app as app
from pyrogram import Client, filters, types
from pyrogram.types import Message
from pyrogram.raw.types import InputFile
from io import BytesIO
from pyrogram.raw.functions.messages import GetStickerSet

TEMP_DOWNLOAD_DIRECTORY = []

@app.on_message(filters.command("mmf"))
async def memify(client, message):
    try:
        chat_id = message.chat.id
        args = message.text.split(" ", 1)

        if len(args) == 1:
            await message.reply_text('Provide some text and reply to image/stickers EXAMPLE: /mmf text')
            return

        xx = await message.reply_text('Memifing your sticker...wait!')

        sticker_set = await app.send(GetStickerSet(stickerset=message.reply_to_message.sticker.set_name))

        if not sticker_set.is_animated:
            await xx.edit_text("Sorry, this function can't work with animated stickers.")
            return

        file_id = message.reply_to_message.sticker.file_id

        with BytesIO() as file:
            file.name = 'mmfsticker.png'
            async for chunk in app.get_file(file_id):
                file.write(chunk)

            file.seek(0)
            img = Image.open(file)

        text = args[1]
        i_width, i_height = img.size
        fnt = "./DAXXMUSIC/assets/font2.ttf" if os.name == "nt" else "./DAXXMUSIC/assets/font.ttf"
        m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))

        upper_text, lower_text = (text.split(";") + [""])[:2]   

        draw = ImageDraw.Draw(img)
        current_h, pad = 10, 5

        for t in [upper_text, lower_text]:
            if t:
                for line in textwrap.wrap(t, width=15):
                    u_width, u_height = draw.textsize(line, font=m_font)
                    for offset in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                        draw.text(xy=(((i_width - u_width) / 2) + offset[0], int((current_h / 640) * i_width) + offset[1]),
                                  text=line, font=m_font, fill=(0, 0, 0))
                    draw.text(xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                              text=line, font=m_font, fill=(255, 255, 255))
                    current_h += u_height + pad

        image_name = "memify.webp"
        webp_file = os.path.join(image_name)
        img.save(webp_file, "webp")
        output = open(image_name, "rb")
        await app.send_sticker(chat_id, InputFile(output), reply_to_message_id=message.message_id)
        await xx.delete()

    except Exception as e:
        await message.reply_text(f'Error Report @Sanam_King, {e}')
