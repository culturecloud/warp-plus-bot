import logging
import requests
from ..vars import var
def ping_server():
    k = requests.get(f'https://ping-pong-sn.herokuapp.com/pingback?link={var.URL}').json()
    if not k.get('error'):
        logging.info('KeepAliveService: {}'.format(k.get('message')))
    else:
        logging.error('KeepAliveService: Couldn\'t Ping the Server!')
