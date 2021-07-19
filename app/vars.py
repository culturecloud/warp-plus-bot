# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class var(object):
    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    BOT_TOKEN = str(getenv('BOT_TOKEN'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL')) if 'BIN_CHANNEL' in environ else None
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    # OWNER_ID = int(getenv('OWNER_ID')) #TODO
    NO_PORT = bool(getenv('NO_PORT', False))
    ON_HEROKU = False
    ON_REPLIT = False
    if 'APP_NAME' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    elif 'REPLIT_APP_NAME' in environ:
        ON_REPLIT = True
        REPLIT_APP_NAME = str(getenv('REPLIT_APP_NAME'))
        REPLIT_USERNAME = str(getenv('REPLIT_USERNAME'))
    else:
        ON_HEROKU = False
        ON_REPLIT = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    REPLIT_FQDN = "{}.{}.repl.co".format(REPLIT_APP_NAME, REPLIT_USERNAME) if ON_REPLIT else None
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else ("https://{}/".format(REPLIT_FQDN) if ON_REPLIT else "http://{}:{}/".format(FQDN, PORT))