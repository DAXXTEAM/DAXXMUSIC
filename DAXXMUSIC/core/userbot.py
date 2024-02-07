from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="DAXXMUSICASS1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="DAXXMUSICASS2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="DAXXMUSICASS3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="SophiaMusic4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="DAXXMUSICASS5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )
        self.six = Client(
            name="DAXXMUSICASS6",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING6),
            no_updates=True,
        )
        self.seven = Client(
            name="DAXXMUSICASS7",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING7),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("AmBotYT")
                await self.one.join_chat("AM_YTSupport")
                await self.one.join_chat("AbhiModszYT_Return")
                await self.one.join_chat("AM_Unfban")
                await self.one.join_chat("Logs_Gban")
                await self.one.join_chat("About_AMBot")
                await self.one.join_chat("Fbans_Logs")
                await self.one.join_chat("SpicyEmpireSupport")
                await self.one.join_chat("SpicyEmpire")
                await self.one.join_chat("SpicyEmpireFban")
                await self.one.join_chat("DAXXSUPPORT")
                await self.one.join_chat("ALLTYPECC")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistant 1 Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("AmBotYT")
                await self.two.join_chat("AM_YTSupport")
                await self.two.join_chat("AbhiModszYT_Return")
                await self.two.join_chat("AM_Unfban")
                await self.two.join_chat("Logs_Gban")
                await self.two.join_chat("About_AMBot")
                await self.two.join_chat("Fbans_Logs")
                await self.two.join_chat("SpicyEmpireSupport")
                await self.two.join_chat("SpicyEmpire")
                await self.two.join_chat("SpicyEmpireFban")
                await self.two.join_chat("DAXXSUPPORT")
                await self.two.join_chat("ALLTYPECC")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant 2 Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("AmBotYT")
                await self.three.join_chat("AM_YTSupport")
                await self.three.join_chat("AbhiModszYT_Return")
                await self.three.join_chat("AM_Unfban")
                await self.three.join_chat("Logs_Gban")
                await self.three.join_chat("About_AMBot")
                await self.three.join_chat("Fbans_Logs")
                await self.three.join_chat("SpicyEmpireSupport")
                await self.three.join_chat("SpicyEmpire")
                await self.three.join_chat("SpicyEmpireFban")
                await self.three.join_chat("DAXXSUPPORT")
                await self.three.join_chat("ALLTYPECC")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant 3 Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("AmBotYT")
                await self.four.join_chat("AM_YTSupport")
                await self.four.join_chat("AbhiModszYT_Return")
                await self.four.join_chat("AM_Unfban")
                await self.four.join_chat("Logs_Gban")
                await self.four.join_chat("About_AMBot")
                await self.four.join_chat("Fbans_Logs")
                await self.four.join_chat("SpicyEmpireSupport")
                await self.four.join_chat("SpicyEmpire")
                await self.four.join_chat("SpicyEmpireFban")
                await self.four.join_chat("DAXXSUPPORT")
                await self.four.join_chat("ALLTYPECC")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant 4 Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("AmBotYT")
                await self.five.join_chat("AM_YTSupport")
                await self.five.join_chat("AbhiModszYT_Return")
                await self.five.join_chat("AM_Unfban")
                await self.five.join_chat("Logs_Gban")
                await self.five.join_chat("About_AMBot")
                await self.five.join_chat("Fbans_Logs")
                await self.five.join_chat("SpicyEmpireSupport")
                await self.five.join_chat("SpicyEmpire")
                await self.five.join_chat("SpicyEmpireFban")
                await self.five.join_chat("DAXXSUPPORT")
                await self.five.join_chat("ALLTYPECC")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant 5 Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

        if config.STRING6:
            await self.six.start()
            try:
                await self.six.join_chat("AmBotYT")
                await self.six.join_chat("AM_YTSupport")
                await self.six.join_chat("AbhiModszYT_Return")
                await self.six.join_chat("AM_Unfban")
                await self.six.join_chat("Logs_Gban")
                await self.six.join_chat("About_AMBot")
                await self.six.join_chat("Fbans_Logs")
                await self.six.join_chat("SpicyEmpireSupport")
                await self.six.join_chat("SpicyEmpire")
                await self.six.join_chat("SpicyEmpireFban")
                await self.six.join_chat("DAXXSUPPORT")
                await self.six.join_chat("ALLTYPECC")
            except:
                pass
            assistants.append(6)
            try:
                await self.six.send_message(config.LOGGER_ID, "Assistant 6 Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 6 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.six.id = self.six.me.id
            self.six.name = self.six.me.mention
            self.six.username = self.six.me.username
            assistantids.append(self.six.id)
            LOGGER(__name__).info(f"Assistant Six Started as {self.six.name}")

        if config.STRING7:
            await self.seven.start()
            try:
                await self.seven.join_chat("AmBotYT")
                await self.seven.join_chat("AM_YTSupport")
                await self.seven.join_chat("AbhiModszYT_Return")
                await self.seven.join_chat("AM_Unfban")
                await self.seven.join_chat("Logs_Gban")
                await self.seven.join_chat("About_AMBot")
                await self.seven.join_chat("Fbans_Logs")
                await self.seven.join_chat("SpicyEmpireSupport")
                await self.seven.join_chat("SpicyEmpire")
                await self.seven.join_chat("SpicyEmpireFban")
                await self.seven.join_chat("DAXXSUPPORT")
                await self.seven.join_chat("ALLTYPECC")
            except:
                pass
            assistants.append(7)
            try:
                await self.seven.send_message(config.LOGGER_ID, "Assistant 7 Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 7 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.seven.id = self.seven.me.id
            self.seven.name = self.seven.me.mention
            self.seven.username = self.seven.me.username
            assistantids.append(self.seven.id)
            LOGGER(__name__).info(f"Assistant Seven Started as {self.seven.name}")

            
