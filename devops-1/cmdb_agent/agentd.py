import logging
import os
import time
from gconf import Config
from utils import fileutils, sysutils, mqueue
from plugins import ens, client, heartbeat, resource

logger = logging.getLogger(__name__)




def main(config):

    ths = {}
    ths['client'] = {'class': client.Client, 'threading': None}
    ths['ens'] = {'class': ens.ENS, 'threading': None}
    ths['heartbeat'] = {'class': heartbeat.Heartbeat, 'threading': None}
    ths['resource'] = {'class': resource.Resource, 'threading': None}

    while True:
        for key, value in ths.items():
            if value['threading'] is None or not value['threading'].is_alive():
                logger.error(f'threading[{key}] is dead and restart.')
                value['threading'] = value['class'](config)
                value['threading'].start()

        time.sleep(3)


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8888
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s : %(message)s',
        filename=os.path.join(PROJECT_PATH, 'logs', 'agentd.log'),
        filemode='a'
    )

    config = Config

    PID = os.getpid()
    setattr(config, 'PROJECT_PATH', PROJECT_PATH)
    setattr(config, 'PID', PID)
    setattr(config, 'HOST', HOST)
    setattr(config, 'PORT', PORT)

    UUID_PATH = os.path.join(PROJECT_PATH, 'UUID')
    UUID = fileutils.read_file(UUID_PATH)
    if not UUID:
        UUID = sysutils.get_uuid()
        fileutils.write_file(UUID_PATH, UUID)
    setattr(config, 'UUID', UUID)
    setattr(config, 'QUEUE', mqueue.Queue())

    logger.info('agentd is starting....')
    logger.info(f'PID: {PID}')
    logger.info(f'UUID: {UUID}')

    main(config)