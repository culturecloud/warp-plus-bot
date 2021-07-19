# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import sys
import glob
import asyncio
import logging
import importlib
from pathlib import Path
from pyrogram import idle
from .bot import BOT
from .vars import var
from aiohttp import web
from .server import web_server
from .utils.keepalive import ping_server
from apscheduler.schedulers.background import BackgroundScheduler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("apscheduler").setLevel(logging.WARNING)

ppath = "app/bot/plugins/*.py"
files = glob.glob(ppath)

loop = asyncio.get_event_loop()


async def start_services():
    print('\n')
    print('------------------- Initalizing Telegram Bot -------------------')
    await BOT.start()
    print('----------------------------- DONE -----------------------------')
    print('\n')
    print('--------------------------- Importing ---------------------------')
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"app/bot/plugins/{plugin_name}.py")
            import_path = ".plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["app.bot.plugins." + plugin_name] = load
            print("Imported => " + plugin_name)
    if var.ON_HEROKU or var.ON_REPLIT:
        print('------------------ Starting Keep Alive Service ------------------')
        print('\n')
        scheduler = BackgroundScheduler()
        int_sec = 1200 if var.ON_HEROKU else 300
        scheduler.add_job(ping_server, "interval", seconds=int_sec)
        scheduler.start()
    print('-------------------- Initalizing Web Server --------------------')
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if var.ON_HEROKU or var.ON_REPLIT else var.FQDN
    await web.TCPSite(app, bind_address, var.PORT).start()
    print('----------------------------- DONE -----------------------------')
    print('\n')
    print('----------------------- Service Started -----------------------')
    print('                        bot =>> {}'.format((await BOT.get_me()).first_name))
    print('                        server ip =>> {}:{}'.format(bind_address, var.PORT))
    if var.ON_HEROKU:
        print('                        app runnng on =>> {}'.format(var.FQDN))
    elif var.ON_REPLIT:
        print('                        app runnng on =>> {}'.format(var.REPLIT_FQDN))
    print('---------------------------------------------------------------')
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')