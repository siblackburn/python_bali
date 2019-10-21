import unittest

from data_structures.doubly_linked_list import DoublyLinkedList

class TestLinkedlist(unittest.TestCase):

    def test_first_item(self):
        test_list = DoublyLinkedList()
        test_list.insert_front(5)
        test_list.insert_front(9)
        pop = test_list.pop_front()

        self.assertEqual(9, pop, "first item did not insert correctly")

    def test_pop_from_front(self):
        test_list = DoublyLinkedList()
        test_list.insert_front(5)
        test_list.insert_front(7)
        test_list.insert_front(9)
        front_pop = test_list.pop_front()

        node = test_list.pop_front()
        self.assertEqual(7, node._node_value, "First item isn't the second item before pop from front")

unittest.main(argv=[''], verbosity=2, exit=False)