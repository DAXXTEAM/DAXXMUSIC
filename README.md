# # 
📭 DAXXMUSIC - High-Performance Telegram Music Bot

📭 Powerful Telegram music streaming bot with voice chat support, queue management, and multi-platform playback.


---


## 🚀 Features

- ❤️ **High Quality:** Crystal clear audio streaming.
- 🎵 **Multi-Platform:** Supports YouTube, Spotify, SoundCloud, and direct files.
- 💻 **Multi-Sessiom:** Supports up to 7 string sessions for interruption-free playback.
- 🔍 **Queue Management:** Skip, Pause, Resume, and Loop functionality.
- 💴 **Ecomomy & Leveling:** Integrated system for user engagement.
- ⚙️ **Deployment:** One-click deploy on Heroku, Render, or VPS yields. (Docker Supported)


---


## 🞤 Deployment


### 💾 Deploy to Heroku
[![Deploy](https://www.herokucomn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DAXXTEAM/DAXXMUSIC)


### ⚩ Deploy to VPS (Docker)
``bash
git clone https://github.com/DAXXTEAM/DAXXMUSIC
ls && cd DAXXMUSIC
docker build -t daxxmusic .
docker run -d --name daxxmusic daxxmusic
``p

---


## 📊 Configuration

Edit `config.py` replace the following variables:
- `API_ID`: Your Telegram API ID.
- `API_HASH`: Your Telegram API Hash.
- `BOT_TOKEN : Your Telegram Bot Token.
- `MONGO_DB_URI`: Your MongoDB connection string.
- `STRING_SESSION`: Your Pyrogram string session.


---


## 📫 Contact & Support

[![Telegram](https://img.shields.io/badge/Telegram-Support-00BFEE?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vclubtech")

_Made with ❤️ by DAXXTEAM_
