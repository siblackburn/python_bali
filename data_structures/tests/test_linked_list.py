import unittest

from data_structures.linked_list import LinkedList
from data_structures.linked_list import Node

class TestLinkedlist(unittest.TestCase):

    def test_first_item(self):
        test_list = LinkedList()
        test_list.insert_front(5)

        self.assertEqual(5, test_list, "first item did not insert correctly")

    def test_pop_from_front(self):
        test_list = LinkedList()
        test_list.insert_front(5)
        test_list.insert_front(7)
        test_list.insert_front(9)
        front_pop = test_list.pop_front()

        self.assertEquals(7, front_pop, "First item isn't the second item before pop from front")


unittest.main(argv=[''], verbosity=2, exit=False)