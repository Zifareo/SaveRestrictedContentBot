#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24419043
API_HASH = 2259dd677c99132d1fdb9b8e6c68a4ce
BOT_TOKEN = 6653136127:AAE4dfXRzH7nHgrixQ7BnWr6KDAaVPShglk
SESSION = 1BVtsOH4BuySAWiSHWh8HxZlNjw0hCW9x70ryP9WgqR-STPoPA4elBk-2QoIO853QOjcAm3xuPP0qC3nT4H1UGEgkw09c-h2UVxu4122bAFW16dyxVlKUIV24gjQwHRHPHPZqLQYL6sI4CMTtpVWMPuC1Bmj6BDiDp_vUzcdNQZv3qDsmollzi4uUIoe6XbqH-0oQ6ALUcfxDPydb70Qq15VhB_rdQF-YUl1AsgAa2fI6_9JOsyRpH-S-5OJWy_BWoUiOYcQdiTS84Uaf20jHJUek29vD0Cp42REI19vqwKtHWsy_-RMdWA50QCMyizSr_mrR44lTP4-O67zoZ9MvcmJuzNHmwkU=
FORCESUB = "DroneBots"
AUTH = 1058482162

sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd saverestrictedcontentbot 
pip3 install -r requirements.txt
python3 -m main

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
