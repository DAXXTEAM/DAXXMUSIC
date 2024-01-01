import os
import textwrap
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters
from pyrogram.raw.types import InputFile
from DAXXMUSIC import app


@app.on_message(filters.command("mmf") & filters.reply)
async def mmf_handler(client, message):
    if not message.reply_to_message or not message.reply_to_message.media:
        await message.reply("Reply to an image/sticker.")
        return

    file_info = message.reply_to_message.document or message.reply_to_message.photo
    file_path = await client.download_media(file_info)

    text = message.text.split("/mmf", maxsplit=1)[1].strip()

    if not text:
        await message.reply("Provide some text to draw!")
        return

    await message.reply("Memifying this image! ✊🏻")

    meme_file = await draw_text(file_path, text)

    await client.send_document(message.chat.id, document=InputFile(meme_file))

    os.remove(file_path)
    os.remove(meme_file)

async def draw_text(image_path, text):
    img = Image.open(image_path)

    i_width, i_height = img.size

    font_path = "arial.ttf" if os.name == "nt" else "./FallenRobot/resources/default.ttf"
    font_size = int((70 / 640) * i_width)
    font = ImageFont.truetype(font_path, font_size)

    upper_text, lower_text = text.split(";") if ";" in text else (text, "")

    draw = ImageDraw.Draw(img)
    pad = 5

    await draw_text_lines(draw, upper_text, font, i_width, i_height, pad, True)
    await draw_text_lines(draw, lower_text, font, i_width, i_height, pad, False)

    output = BytesIO()
    img.save(output, format="WEBP")

    return output.getvalue()

async def draw_text_lines(draw, text, font, i_width, i_height, pad, is_upper_text):
    current_h = 10 if is_upper_text else i_height - int((20 / 640) * i_width)

    for line in textwrap.wrap(text, width=15):
        text_width, text_height = draw.textsize(line, font=font)

        for offset in [(-2, 0), (2, 0), (0, -2), (0, 2), (0, 0)]:
            draw.text(
                xy=(
                    ((i_width - text_width) / 2) + offset[0],
                    current_h + offset[1],
                ),
                text=line,
                font=font,
                fill=(0, 0, 0) if is_upper_text else (255, 255, 255),
            )

        draw.text(
            xy=((i_width - text_width) / 2, current_h),
            text=line,
            font=font,
            fill=(255, 255, 255) if is_upper_text else (0, 0, 0),
        )

        current_h += text_height + pad
