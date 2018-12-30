from queue import Queue, Empty, Full


class PyQueue(Queue):
    def put(self, item, block=True, timeout=None):
        try:
            super().put(item, block, timeout)
            return True
        except Full as e:
            return False

    def get(self, block=True, timeout=None):
        try:
            return super().get(block, timeout)
        except Empty as e:
            return None

    def qsize(self):
        return super().qsize()


class RedisQueue:
    pass


class MyQueue:
    pass


Queue = PyQueue
