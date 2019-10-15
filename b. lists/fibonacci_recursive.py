'''
def my_func(i):
    if i == 0:
        return
    print("hi world")
    my_func(i-1)

my_func(10)
'''


def fib_numbers(i):
    if i <= 1:
        return 1
    else:
        return fib_numbers(i-1) + fib_numbers(i-2)

print(fib_numbers(100))

# creating a list of fibonacci numbers using a generator
print([fib_numbers(i) for i in range(15)])



