import threading
import time
import logging
import importlib
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')


def worker():
    logging.info('starting')
    time.sleep(2)
    logging.info('completed')


t = threading.Thread(target=worker, daemon=True)
t.start()
