from app.bot import BOT
from pyrogram import filters

@BOT.on_message(filters.incoming and filters.private and filters.command('about'))
def about(bot, message):
    message.reply("The original script for getting free WARP+ bandwidth was written by @aliilapro and then implemented as a Telegram bot by @pseudokawaii.\n\n**Original Project Source** : https://github.com/ALIILAPRO/warp-plus-cloudflare\n\n**Bot Source** : https://github.com/culturecloud/warp-plus-bot", disable_web_page_preview=True)