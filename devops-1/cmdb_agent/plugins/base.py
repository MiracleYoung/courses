import logging
import threading
import time
import psutil
import platform

from utils import sysutils

logger = logging.getLogger(__name__)


class BasePlugin(threading.Thread):
    def __init__(self, config, interval=60, name='plugin', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.daemon = True
        self.config = config
        self.interval = interval

    def run(self):
        _config = self.config
        _queue = getattr(_config, 'QUEUE')
        _interval = self.interval
        while True:
            _msg = self.make_msg()
            if _msg:
                _queue.put(_msg)
            time.sleep(_interval)

    def make_msg(self):
        return None