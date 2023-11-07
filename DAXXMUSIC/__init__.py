from DAXXMUSIC.core.bot import DAXX
from DAXXMUSIC.core.dir import dirr
from DAXXMUSIC.core.git import git
from DAXXMUSIC.core.userbot import Userbot
from DAXXMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DAXX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
