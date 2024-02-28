from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ᴀᴅᴅ ᴍᴇ🥀",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🍂ᴏᴡɴᴇʀ🍂",url=f"https://t.me/PAWAN_IS_BACK"),
            InlineKeyboardButton(text="🍃ᴜᴘᴅᴀᴛᴇ🍃", url=f"https://t.me/angel_world11"),
        ],
        [  
            InlineKeyboardButton(text="💕sᴜᴘᴘᴏʀᴛ💕", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="💸ʀᴇᴘᴏ💸", callback_data="gib_source"),
        ],
        [
            InlineKeyboardButton(text="🚀ʜᴇʟʟ & ᴄᴍᴅs🚀", callback_data="settings_back_helper"),
        ],
    ]
    return buttons
    
