'''
- Write a function to reverse a string
'''
my_string = "hello world"

def reverse_fn(x):
    x = x[::-1]
    return x

output = reverse_fn(my_string)
print(output)