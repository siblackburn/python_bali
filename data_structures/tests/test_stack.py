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
