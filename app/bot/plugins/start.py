# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from app.bot import BOT
from pyrogram import filters


@BOT.on_message(filters.incoming and filters.private and filters.command('start'))
def start(bot, message):
    message.reply("Hello **{}**, I can give you **FREE UNLIMITED** WARP+ bandwidth on [Cloudflare WARP](https://1.1.1.1/). Send a /help command to know how.".format(message.from_user.first_name))