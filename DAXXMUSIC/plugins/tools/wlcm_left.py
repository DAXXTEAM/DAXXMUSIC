from DAXXMUSIC import app
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont

# --------------------------------------------------------------------------------- #

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
                ])
            )
        except RPCError as e:
            print(e)
            return
    else:
        # Handle the case where the user has no profile photo
        print(f"User {user.id} has no profile photo.")
        
