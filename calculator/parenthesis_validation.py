'''
Write a function that validates matching parenthesis in a prefix notation formula.
Valid:
`(+ 1 2)`
Invalid:
`(+ 1 2)(`
In general, we are trying to validate that each open parenthesis, should have a corresponding closed parenthesis. hint: use a stack.
'''

'''
Import Stack class from previous exercise
Define the input to test
create an empty stack
'''

from data_structures.stack import Stack
my_input = "(+ 1 2)(((("

stack1 = Stack()

'''
Define function to test the input.
if stack has any unmatched parentheses at the end of the function, function will return False, meaning the input is invalid
'''

def parenthesis_check(x):
    for items in x:
        if items == "(":
            stack1.push(items)
        if items == ")" and len(stack1) == 0:
            return f'there weren"t enough open brackets to compliement the closed brackets'
        if items == ")":
            stack1.pop()
    if stack1.__len__() == 0:
        return True
    return False


test = parenthesis_check(my_input)
print(test)

'''
Quick check to see what is left in the stack. These are any unmatched parentheses
'''
print(stack1.__repr__())

