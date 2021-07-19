from app.bot import BOT
from pyrogram import filters

@BOT.on_message(filters.incoming and filters.private and filters.command('about'))
def about(bot, message):
    message.reply("The original code for getting free WARP+ bandidth was written by @aliilapro and then implemented as a Telegram bot by @pseudokawaii.\n\nOriginal Project: https://github.com/ALIILAPRO/warp-plus-cloudflare")