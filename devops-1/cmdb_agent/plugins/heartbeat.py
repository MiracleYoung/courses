import logging
import time
from plugins import base

logger = logging.getLogger(__name__)


class Heartbeat(base.BasePlugin):
    def __init__(self, config, *args, **kwargs):
        super().__init__(config, name='heartbeat', interval=10, *args, **kwargs)

    def make_msg(self):
        msg = {
            'type': 'heartbeat',
            'content': {
                'time': time.time()
            }

        }
        logger.debug(f'msg : {msg}')
        return msg
