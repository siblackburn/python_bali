import unittest

from data_structures.stack import Stack


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        
        # Arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        
        # Act
        pop1 = my_stack.pop()
        pop2 = my_stack.pop()
        
        # Assert
        self.assertEqual(2, pop1, "first pop did not have the expected value")
        self.assertEqual(1, pop2, "second pop did not have the expected value")
        # self.assertTrue(type(my_stack) == type(list), "type should have been a stack")


    def test_stack_length(self):
        #arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)

        #assert
        self.assertEqual(2, len(my_stack), "stack length does not return the correct length")

    def test_pop_error(self):

        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.pop()
        my_stack.pop()
        self.assertRaises(Exception, my_stack.pop)
        # If it is, then the test has run as it should be. Because we're testing that popping 3 times and pushing 2 times doesn't work




unittest.main(argv=[''], verbosity=2, exit=False)
