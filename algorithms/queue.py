from collections import deque


class AbstractQueue(object):

    def __init__(self):
        self.max_size = 0
        self.items = None

    def put(self):
        raise NotImplementedError()

    def get(self):
        raise NotImplementedError()

    def qsize(self):
        return len(self.items)

    def empty(self):
        return not self.qsize()

    def full(self):
        return self.qsize() == self.max_size


class Queue(AbstractQueue):

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.items = deque([])

    def put(self, item):
        self.items.append(item)

    def get(self):
        if self.empty():
            raise IndexError('Queue is empty')
        return self.items.popleft()



