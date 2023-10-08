from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="DAXXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="DAXXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="DAXXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="DAXXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="DAXXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"🌿𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭  𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("cyberdaxxx")
                await self.one.join_chat("cyberdaxx")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "**╔═══❰🎭𝗗𝗔𝗫𝗫 𝗧𝗘𝗔𝗠🎭❱═══❍⊱❁۪۪**\n**║**\n**║┣⪼🍫𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝🧨**\n**║**\n**║┣⪼🎫𝐈𝐝:- {self.one.id}**\n**║**\n**║┣⪼🏆𝐔-𝐍:- @{self.one.username}**\n**║ **\n**║┣⪼🧸𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠♥️**\n**║**\n**╚══════════════❍⊱❁")
            except:
                LOGGER(__name__).error(
                    "🌱𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐈𝐬 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩, 𝐆𝐨 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐀𝐝𝐦𝐢𝐧 𝐓𝐡𝐞𝐧 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐖𝐨𝐫𝐤🏵️🏵️"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 1 𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨 {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("cyberdaxxx")
                await self.one.join_chat("cyberdaxx")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭  𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 2 𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨 {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("cyberdaxxx")
                await self.one.join_chat("cyberdaxx")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭  𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 3 𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨 {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("cyberdaxxx")
                await self.one.join_chat("cyberdaxx")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭  𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 4 𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨 {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("cyberdaxxx")
                await self.one.join_chat("cyberdaxx")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭  𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 5 𝐒𝐭𝐚𝐫𝐭𝐞𝐝......🧨 {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 1 𝐒𝐭𝐨𝐩🚫......🧨")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
