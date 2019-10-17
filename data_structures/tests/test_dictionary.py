import unittest

from data_structures.dictionary import Dictionary


class TestQueue(unittest.TestCase):
    '''
    Test to check we can assign an index
    '''

    def test_get_index(self):
        my_dict = Dictionary()
        my_dict.get_index("hi")

        self.assertTrue(my_dict.get_index("hi") >= 0, "'  hi' does not have an index. get_index function may be broken")

    '''
    Test to check that if we pass an item, it stores it
    Test to check that if we pass an item it gets given a corresponding key
    '''

    def test_set(self):
        my_dict = Dictionary()
        my_dict.set("hi", "old world")
        my_dict.set("hi", "world")

        self.assertTrue(my_dict.get_index("hi"), "hi has an index")
        self.assertNotEqual("old world", my_dict.get("hi"), "hi shouldn't return 'old world'. Check to see if old world still exists")

    '''
    Test to check that if we call a key, it returns the corresponding item
    '''

    def test_get(self):
        my_dict = Dictionary()
        my_dict.set("hi", "world")

        self.assertTrue(my_dict.get("hi") == "world",  "get function does not return the correct value")

    '''
    Test to check we can call the items 
    '''
    def test_contains(self):
        my_dict = Dictionary()
        my_dict.set("a", 25)

        self.assertTrue(my_dict.contains("a"), "contains method is broken")

    '''
    test to check the delete function. It should remove the tuple from the list
    '''
    def test_delete(self):
        my_dict = Dictionary()
        my_dict.set("a", 24)
        my_dict.set("b", 30)
        my_dict.set("c", 40)
        my_dict.delete("b")

        self.assertNotEqual(my_dict.contains("b"), "b was not removed from the list")
        self.assertTrue(my_dict.contains("a"), "a was deleted when it shouldn't have been")

    '''
    Test to check that the number of items in the dictionary is equal to the number of items we passed it
    '''

    def test_many_keys(self):
        my_dict = Dictionary()
        for numbers in range(0, 1000):
            my_dict.set(numbers, numbers)

        self.assertEqual(999, my_dict.get(999), "test failed")

unittest.main(argv=[''], verbosity=2, exit=False)