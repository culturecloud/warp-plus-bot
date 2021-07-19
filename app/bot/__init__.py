# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import Client
from ..vars import var

BOT = Client(
    session_name= ':memory:',
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    sleep_threshold=var.SLEEP_THRESHOLD,
    workers=var.WORKERS
)