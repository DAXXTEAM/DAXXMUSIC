
from functools import wraps 

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus, ChatType

from DAXXMUSIC import app

from config import OWNER_ID, BOT_USERNAME
from DAXXMUSIC.misc import SUDOERS

COMMANDERS = [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]

from typing import Tuple

async def user_has_permission(chat_title: str, chat_id: int, user_id: int, permission: str, bot=True) -> Tuple[bool, str]:
    


#async def user_has_permission(chat_title : str, chat_id: int, user_id: int, permission: str,bot=True) -> tuple[bool, str]:
    try:
        if user_id in SUDORES:
            have_permission = True
        else:
            chat_member = await app.get_chat_member(chat_id, user_id)
            chat_permissions = chat_member.privileges
            if permission == "can_delete_messages":
                have_permission = chat_permissions.can_delete_messages
            elif permission == "can_manage_chat":
                have_permission = chat_permissions.can_manage_chat
            elif permission == "can_manage_video_chats":
                have_permission = chat_permissions.can_manage_video_chats
            elif permission == "can_restrict_members":
                have_permission = chat_permissions.can_restrict_members
            elif permission == "can_promote_members":
                have_permission = chat_permissions.can_promote_members
            elif permission == "can_change_info":
                have_permission = chat_permissions.can_change_info
            elif permission == "can_post_messages":
                have_permission = chat_permissions.can_post_messages
            elif permission == "can_edit_messages":
                have_permission = chat_permissions.can_edit_messages
            elif permission == "can_invite_users":
                have_permission = chat_permissions.can_invite_users
            elif permission == "can_pin_messages":
                have_permission = chat_permissions.can_pin_messages    
            else:
                have_permission = False

    except Exception as e:
        print(e)
        have_permission = False

    if not have_permission:
        if bot:
            txt = f"I Don't Have The Following Right:\n**[{permission}]**\nIn **{chat_title}**."
        else:
            txt = f"You Don't Have The Following Right:\n{permission}\nIn {chat_title}. So You Cant Perform This Action"
        return have_permission, txt
    else:
        return have_permission, None


def bot_admin(func):
    @wraps(func)
    async def is_bot_admin(app : Client, message : Message,*args,**kwargs):
        chat_type = message.chat.type
        if chat_type == ChatType.PRIVATE:
            return await message.reply("Use This Command In Groups")
        BOT = await app.get_chat_member(message.chat.id,BOT_USERNAME)                 
        if BOT.status != ChatMemberStatus.ADMINISTRATOR:                                       
            await message.reply_text(f"I Am Not Admin In **{message.chat.title}**")
            return 
        return await func(app,message,*args,**kwargs)
    return is_bot_admin

def bot_can_ban(func):
    @wraps(func)
    async def can_restrict(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_USERNAME)
                 
        if not BOT.privileges.can_restrict_members:                        
            await message.reply_text(f"I Don't Have Rights To Restrict The User In **{message.chat.title}**.")
            return 
        return await func(app,message,*args,**kwargs)
    return can_restrict

def bot_can_change_info(func):
    @wraps(func)
    async def can_change_info(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_USERNAME)

        if not BOT.privileges.can_change_info:                         
            await message.reply_text(f"I Don't Have Rights To Change Info In **{message.chat.title}**.")
            return 
        return await func(app,message,*args,**kwargs)
    return can_change_info


def bot_can_promote(func):
    @wraps(func)
    async def can_promote(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_USERNAME)

        if not BOT.privileges.can_promote_members:                         
            await message.reply_text(f"I Don't Have Rights To Promote Users In **{message.chat.title}**.")
            return 
        return await func(app,message,*args,**kwargs)
    return can_promote


def bot_can_pin(func):
    @wraps(func)
    async def can_pin(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_USERNAME)

        if not BOT.privileges.can_pin_messages:                         
            await message.reply_text(f"I Don't Have Rights To Pin Messages In **{message.chat.title}**.")
            return 
        return await func(app,message,*args,**kwargs)
    return can_pin

def bot_can_del(func):
    @wraps(func)
    async def can_delete(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_USERNAME)

        if not BOT.privileges.can_delete_messages:                         
            await message.reply_text(f"I Don't Have Rights To Delete Messages In **{message.chat.title}**.")
            return 
        return await func(app,message,*args,**kwargs)
    return can_delete

def user_admin(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        chat_type = message.chat.type
        if chat_type == ChatType.PRIVATE:
            return await message.reply("Use This Command In Groups Only")
        if message.sender_chat:
            if message.sender_chat.id == message.chat.id:
                return await message.reply("You Are Anonymous Admin Please Use User ID")
            else:
                return await message.reply_text("You Are Not Admin")
                
        else:
            user_id = message.from_user.id    
            chat_id = message.chat.id
            user = await app.get_chat_member(chat_id,user_id) 
        
            if (user.status not in COMMANDERS) and user_id not in SUDORES:
                return await message.reply_text("You Are Not Admin")
                                                                            
        return await mystic(app,message,*args,**kwargs)

    return wrapper

def user_can_ban(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.privileges and not user.privileges.can_restrict_members) and user_id not in SUDORES: 

            return await message.reply_text("You Dont Have Right To Restrict Users.") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper

def user_can_del(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.status in COMMANDERS and not user.privileges.can_delete_messages) and user_id not in SUDORES:                     
            return await message.reply_text("You Dont Have Right To Delete Messages") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper
            

def user_can_change_info(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.status in COMMANDERS and not user.privileges.can_change_info) and user_id not in SUDORES:                     
            return await message.reply_text("You Dont Have Right To Change Info Of This Group.") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper
            
def user_can_promote(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.status in COMMANDERS and not user.privileges.can_promote_members) and user_id not in SUDORES:                     
            return await message.reply_text("You Dont Have Right To Promote Users Of This Group.") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper
        
