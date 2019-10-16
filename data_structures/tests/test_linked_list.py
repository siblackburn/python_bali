import unittest

from data_structures.linked_list import LinkedList


class TestLinkedlist(unittest.TestCase):

    def test_first_item(self):
        test_list = LinkedList()
        test_list.insert_front(5)

        self.assertEqual(5, test_list.pop_front()._node_value, "first item did not insert correctly")

    def test_pop_from_front(self):
        test_list = LinkedList()
        test_list.insert_front(5)
        test_list.insert_front(7)
        test_list.insert_front(9)
        front_pop = test_list.pop_front()

        node = test_list.pop_front()
        self.assertEqual(7, node._node_value, "First item isn't the second item before pop from front")

    def test_delete_any(self):
        test_list = LinkedList()
        test_list.insert_front(5)
        test_list.insert_front(7)
        test_list.insert_front(9)
        test_list.insert_front(7)
        test_list.delete_item(7)

        self.assertEqual(True, test_list.__contains__(7), "7 was not deleted")

    def test_reversing_list(self):
        test_list = LinkedList()
        test_list.insert_front(5)
        test_list.insert_front(7)
        test_list.insert_front(9)

        test_list.reverse_list()
        node = test_list.pop_front()

        self.assertEqual(5, node._node_value, "list was not reversed")

unittest.main(argv=[''], verbosity=2, exit=False)