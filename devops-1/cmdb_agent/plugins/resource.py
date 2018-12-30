import logging
import threading
import time
import psutil

from plugins import base

from utils import sysutils

logger = logging.getLogger(__name__)


class Resource(base.BasePlugin):
    def __init__(self, config, *args, **kwargs):
        super().__init__(config, name='resource', interval=60, *args, **kwargs)

    def make_msg(self):
        msg = {
            'type': 'resource',
            'content': {
                'cpu': psutil.cpu_percent(),
                'mem': psutil.virtual_memory().percent,
            }

        }
        logger.debug(f'msg : {msg}')
        return msg
