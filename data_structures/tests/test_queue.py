import unittest

from data_structures.queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue_remove(self):

        my_queue = Queue()
        my_queue.enqueue(5)
        my_queue.enqueue(7)
        my_queue.enqueue(9)
        deque_test = my_queue.dequeue()

        self.assertEqual(5, deque_test, "dequeue did not remove the first item")


    def test_length_queue(self):
        my_queue = Queue()
        my_queue.enqueue(5)
        my_queue.enqueue(7)
        my_queue.enqueue(9)

        self.assertTrue(len(my_queue) == 3, "length of the queue was not as expected")


    def test_queue_last_item(self):
        my_queue = Queue()
        my_queue.enqueue(5)

        self.assertTrue(len(my_queue) >0, "Queue is empty")


unittest.main(argv=[''], verbosity=2, exit=False)