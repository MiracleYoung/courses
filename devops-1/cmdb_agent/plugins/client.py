import logging
import threading
import time
import psutil
import platform

from utils import sysutils
from plugins import base

logger = logging.getLogger(__name__)


class Client(base.BasePlugin):
    def __init__(self, config, *args, **kwargs):
        super().__init__(config, interval=60, name='client', *args, **kwargs)

    def make_msg(self):
        msg = {
            'type': 'register',
            'content': {
                'hostname': sysutils.get_hostname(),
                'ip': sysutils.get_ip_address(),
                'mac': sysutils.get_mac_address(),
                'cpu': psutil.cpu_count(),
                'mem': psutil.virtual_memory().total,
                'platform': platform.platform(),
                'arch': platform.architecture()[0],
                'pid': getattr(self.config, 'PID'),
                'time': time.time()
            }

        }
        logger.debug(f'msg : {msg}')
        return msg
