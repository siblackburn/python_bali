'''
Write a function that finds all the matching parenthesis. Let's use string indeces to identify each parenthesis.

For example:
`(+ 1 2)` -> (0, 6)

parenthesis at position 0 matches with parenthesis at position 6

`(* (+ 1 2) 2)` -> [(0, 12), (3, 9)]

parenthesis at position 0 matches with parenthesis at position 12
parenthesis at position 3 matches with parenthesis at position 9

hint: use a stack.
'''


from data_structures.stack import Stack

my_input = "(* (+ 1 2) 2))()(+68)"

stack1 = Stack()

def parenthesis_position(x):
    count = 0
    for items in x:
        if items == "(":
            stack1.push(count)
        if items == ")" and stack1.__len__() == 0:
            print(f'Error: Too many closed brackets before open brackets')
            break
        if items == ")":
            print(f'parenthesis at position {stack1.pop()} matches with parenthesis at {count}')
        count += 1

    if stack1.__len__() != 0:
        print(f'there were {stack1.__len__()} too many open brackets at position {stack1.__repr__()}')
    return

output = parenthesis_position(my_input)




