from app.bot import BOT
from pyrogram import filters
from app.utils import warp

@BOT.on_message(filters.incoming and filters.private and filters.regex(r"[a-zA-Z0-9]+-[a-zA-Z0-9]+-[a-zA-Z0-9]+-[a-zA-Z0-9]+-[a-zA-Z0-9]+|[a-zA-Z0-9]+-[a-zA-Z0-9]+-[a-zA-Z0-9]+"))
async def main(bot, message):
    device_id = message.text
    if len(device_id.split(' ')) != 1:
        await message.reply("Only 1 device ID at a time is supported.")
    else:
        wait_msg = await message.reply("Device ID `{}` has been recieved.\n\nWait a moment ...".format(device_id))
        response = warp.plus(device_id)
        if response.getcode() == 200:
            await wait_msg.edit("1 GB WARP+ bandwidth has been sent to device `{}`.\n\nYou should get a notification from the WARP app if it's a mobile device. Resend the device ID if you didn't get the bandwidth.".format(device_id))
        elif response.code == 429:
            await wait_msg.edit("Slow down! stop spamming and try again after a few minutes.")
        else:
            await wait_msg.edit("ERROR! Please try again later.\n\n<pre>{}</pre>".format(response))