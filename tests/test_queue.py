import unittest
from algorithms.queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue(self):
        q = Queue()
        self.assertEqual(q.empty(), True)

        q.put(0)
        q.put(1)
        self.assertEqual(q.get(), 1)
        self.assertEqual(q.qsize(), 1)
        self.assertEqual(q.empty(), False)

        for i in range(2, 10):
            print(i)
            q.put(i)

        self.assertEqual(q.full(), True)

    def test_queue(self):
        q = Queue()
        self.assertRaises(IndexError, q.get)
