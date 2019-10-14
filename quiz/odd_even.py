'''Write a function that determines if a number is odd or even
'''

user_input = int(input("enter a number:"))

def odd_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

output = odd_even(user_input)
print(output)