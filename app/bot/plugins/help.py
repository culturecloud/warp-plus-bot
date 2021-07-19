from app.bot import BOT
from pyrogram import filters

@BOT.on_message(filters.incoming and filters.private and filters.command('help'))
def help(bot, message):
    message.reply("I use your device ID where Cloudflare WARP app is installed as a referrer and make an API request to Cloudflare, so you get 1 GB WARP+ data on every request.\n\nSo, just send me your device ID which should look something like this ~\n\n`7b029773-a089-4c51-b70f-b55ab48884cb`\n\nOr this ~\n\n`j3X8GM26-4UWh0R57-9iE31c0y`\n\n__Note: Only 1 ID at a time is supported.__")