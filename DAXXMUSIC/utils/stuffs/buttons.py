from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("ᴅɪᴄᴇɢᴀᴍᴇ", callback_data="mplus HELP_DICEGAME"),InlineKeyboardButton("ɢʀᴏᴜᴘs", callback_data="mplus HELP_GROUPS"),InlineKeyboardButton("ɪᴍᴀɢᴇ‌", callback_data="mplus HELP_IMAGE")],
    [InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="mplus HELP_EXTRA")
    ],
    [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"managebot123 settings_back_helper")]]
