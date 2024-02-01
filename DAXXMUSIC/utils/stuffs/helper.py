# helper for strings

class Helper(object):
    HELP_M = '''ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.
ᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /'''
    HELP_DICEGAME = '''ᴅɪᴄᴇɢᴀᴍᴇ

ᴅɪᴄᴇɢᴀᴍᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:
/dice - ᴅɪᴄᴇ 🎲
/dart - ᴅᴀʀᴛ 🎯
/basket - ʙᴀsᴋᴇᴛ ʙᴀʟʟ 🏀
/ball - ʙᴏᴡʟɪɴɢ ʙᴀʟʟ 🎳
/football - ғᴏᴏᴛʙᴀʟʟ ⚽
/jackpot - sᴘɪɴ sʟᴏᴛ ᴍᴀᴄʜɪɴᴇ 🎰
'''
    HELP_IMAGE = '''ɪᴍᴀɢᴇ

ɪᴍᴀɢᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:

/figlet = ᴍᴀᴋᴇs ғɪɢʟᴇᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
/fonts <text> or /font <text> = ᴄᴏɴᴠᴇʀᴛs sɪᴍᴩʟᴇ ᴛᴇxᴛ ᴛᴏ ʙᴇᴀᴜᴛɪғᴜʟ ᴛᴇxᴛ ʙʏ ᴄʜᴀɴɢɪɴɢ ɪᴛ's ғᴏɴᴛ.
/image = ғɪɴᴅ sᴏᴍᴇ ᴘɪᴄᴛᴜʀᴇs ғʀᴏᴍ ᴘɪɴᴛʀᴇsᴛ.
/pic = ɢᴇɴᴇʀᴀᴛᴇ ᴘɪᴄ ғʀᴏᴍ ᴜɴsᴘʟᴀsʜ.
'''
    HELP_GROUPS = '''ɢʀᴏᴜᴘs

ɢʀᴏᴜᴘs ᴄᴏᴍᴍᴀɴᴅꜱ:
/groupdata = ɪᴛ sʜᴏᴡs ʜᴏᴡ ᴍᴀɴʏ ʙᴏᴛs, ᴜsᴇʀs, ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs, ʙᴀɴɴᴇᴅ ᴜsᴇʀs ᴀɴᴅ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
/groupinfo = ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴄʜᴇᴄᴋ ᴏᴛʜᴇʀs ᴘᴜʙʟɪᴄ ɢʀᴏᴜᴘ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
'''
    HELP_EXTRA = '''ᴇxᴛʀᴀ

ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:

/day = ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴅᴀʏ ᴏғ ᴛʜᴇ ᴅᴀᴛᴇ. ᴇxᴀᴍᴘʟᴇ : /day 2006-12-19
/genbin = ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴜsᴇ ғᴏʀ ɢᴇɴᴇʀᴀᴛᴇ ʙɪɴ ғᴏʀ ᴠɪsᴀ, ᴍᴀsᴛᴇʀᴄᴀʀᴅ ᴀɴᴅ ᴅɪsᴄᴏᴠᴇʀ
/genpassword or /genpw = ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ᴜɴɪǫᴜᴇ ᴘᴀssᴡᴏʀᴅ ғʀᴏᴍ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.
/hastag = ᴇɴᴛᴇʀ ᴡᴏʀᴅ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ʜᴀsᴛᴀɢ. ᴇxᴀᴍᴘʟᴇ : /hastag champu
/ipinfo = ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏғ ᴀɴʏ ɪᴘ ᴀᴅᴅʀᴇss. ᴇxᴀᴍᴘʟᴇ : /ipinfo 8:8:8:8
/qr = ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ɪɴᴛᴏ ǫʀᴄᴏᴅᴇ. ᴇxᴀᴍᴘʟᴇ : /qr <link>
/yt or /video = ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ. ᴇxᴀᴍᴘʟᴇ : /yt <youtube-link>
/whisper = ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀs ᴀ ᴡʜɪsᴘᴇʀ ʙᴏᴛ.
/weather = ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄʜᴇᴄᴋ ᴡᴇᴀᴛʜᴇʀ ᴏғ ᴀɴʏ ᴄɪᴛʏ. ᴇxᴀᴍᴘʟᴇ : /weather Delhi 
/Whatsapp = ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ ʟɪɴᴋ ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. ᴇxᴀᴍᴘʟᴇ : /whatsapp +91000000000
'''

    
    
    fullpromote = {
    'can_change_info': True,
    'can_post_messages': True,
    'can_edit_messages': True,
    'can_delete_messages': True,
    'can_invite_users': True,
    'can_restrict_members': True,
    'can_pin_messages': True,
    'can_promote_members': True,
    'can_manage_chat': True,
}

    promoteuser = {
    'can_change_info': False,
    'can_post_messages': True,
    'can_edit_messages': True,
    'can_delete_messages': False,
    'can_invite_users': True,
    'can_restrict_members': False,
    'can_pin_messages': False,
    'can_promote_members': False,
    'can_manage_chat': True,
    }
