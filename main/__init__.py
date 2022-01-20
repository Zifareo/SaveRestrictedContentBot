#ChauhanMahesh/Vasusen/DroneBots/COL

import sys, time, logging
from decouple import config

from telethon import TelegramClient

from pyrogram import Client

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

robot = Client('robot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)