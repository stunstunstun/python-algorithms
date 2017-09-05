

class AbstractQueue(object):

    def __init__(self):
        self.head = 0
        self.size = 0
        self.items = []

    def put(self):
        raise NotImplementedError()

    def get(self):
        raise NotImplementedError()

    def qsize(self):
        return self.size;

    def empty(self):
        return not self.qsize()

    def full(self):
        return self.qsize() == self.size


class Queue(AbstractQueue):

    def __init__(self, capacity=10):
        self.head = 0
        self.size = 0
        self.items = [None] * capacity

    def put(self, item):
        self.items[(self.head + self.size) % len(self.items)] = item
        self.size += 1

    def get(self):
        if self.empty():
            raise IndexError('Queue is empty')
        self.size -= 1
        result = self.items[self.head]
        self.head = (self.head + 1) % len(self.items)
        return result


