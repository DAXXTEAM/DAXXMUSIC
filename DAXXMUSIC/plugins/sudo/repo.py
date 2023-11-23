import asyncio

from pyrogram import filters

import config
from DAXXMUSIC import app
from DAXXMUSIC.misc import SUDOERS
from DAXXMUSIC.utils.formatters import convert_bytes





@app.on_message(filters.command(["repo"]) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.."
    )
    up_r = f"[𝗥𝗘𝗣𝗢]({config.UPSTREAM_REPO})"
    up_b = f"[𝗠𝗔𝗦𝗧𝗘𝗥]({config.UPSTREAM_BRANCH})"
    sp_c = f"[𓆩𓆩〭〬𝗗𝗔𝗫𝗫𝗖𝗖 💳]({config.SUPPORT_CHANNEL})"
    sp_g = f"[𓊈𒆜彡[𝐃𝚊𝚡𝚡 𝐂𝚌 𝐂𝚕𝚞𝚋]彡𒆜𓊉]config.SUPPORT_CHAT})"
    ow_i = f"[𒆜𝐌𝚁°᭄𝐃𝙰𝚇𝚇 ࿐™](https://t.me/iam_daxx)"

 ##############
 
    text = f"""𝗬𝗨𝗠𝗜𝗞𝗢𝗢 𝗕𝗢𝗧 𝗥𝗘𝗣𝗢⌫

    
<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎𝗠𝗥 𝗗𝗔𝗫𝗫:</u>

𝗥𝗘𝗣𝗢 ❥︎ {up_r}

𝗕𝗥𝗔𝗡𝗖𝗘 ❥︎ {up_b}

𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❥︎ {sp_c}

𝗚𝗥𝗢𝗨𝗣 ❥︎ {sp_g}

𝗢𝗪𝗡𝗘𝗥 ❥︎ {ow_i}

    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
