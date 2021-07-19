from app.bot import BOT
from pyrogram import filters

@BOT.on_message(filters.incoming and filters.private and filters.command('faq'))
def faq(bot, message):
    message.reply("**1. What is Cloudflare WARP?**\n\n`Cloudflare WARP is a security-conscious tool for exposing web applications without needing to expose the server they run on. With Cloudflare WARP, traffic to your application is run over a private, encrypted, virtual tunnel from the Cloudflare edge and traffic is only able to find and access your server if it routes through Cloudflare. WARP uses 1.1.1.1 to encrypt your DNS requests and leverages Cloudflares global network of data centers and a more modern protocol to make your internet even faster.`\n\n**2. What is WARP+?**\n\n`WARP+ is WARP, but better. With WARP+, Cloudflare routes your internet requests through globally distributed high performance servers to avoid Internet traffic jams, making it even better. WARP+ runs on a limited data plan.`")