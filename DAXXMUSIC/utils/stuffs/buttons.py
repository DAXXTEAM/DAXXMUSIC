from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("𝐂𝐇𝐀𝐓𝐆𝐓𝐏", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("𝐆𝐑𝐎𝐔𝐏𝐒", callback_data="mplus HELP_Group"),InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("𝐓𝐀𝐆-𝐀𝐋𝐋", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("𝐈𝐍𝐅𝐎", callback_data="mplus HELP_Info"),InlineKeyboardButton("𝐄𝐗𝐓𝐑𝐀", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("𝐈𝐌𝐀𝐆𝐄", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("𝐀𝐂𝐓𝐈𝐎𝐍", callback_data="mplus HELP_Action"),InlineKeyboardButton("𝐒𝐄𝐀𝐑𝐂𝐇", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("𝐅𝐎𝐍𝐓", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("𝐆𝐀𝐌𝐄𝐒", callback_data="mplus HELP_Game"),InlineKeyboardButton("𝐓-𝐆𝐑𝐀𝐏𝐇", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("𝐈𝐌𝐏𝐎𝐒𝐓𝐄𝐑", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("𝐓𝐑𝐔𝐓𝐇-𝐃𝐀𝐑𝐄", callback_data="mplus HELP_TD"),InlineKeyboardButton("𝐇𝐀𝐒𝐓𝐀𝐆", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("𝐓𝐓𝐒", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("𝐅𝐔𝐍", callback_data="mplus HELP_Fun"),InlineKeyboardButton("𝐐𝐔𝐎𝐓𝐋𝐘", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]
