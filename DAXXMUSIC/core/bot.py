from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class DAXX(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="DAXXMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜ sᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except Exception as ex:
            LOGGER(__name__).warning(
                f"Bot could not send to log group/channel (non-fatal): {type(ex).__name__}"
            )

        try:
            a = await self.get_chat_member(config.LOGGER_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).warning(
                    "Bot is not admin in log group/channel (non-fatal)."
                )
        except Exception:
            LOGGER(__name__).warning("Could not check admin status in log group (non-fatal).")

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
