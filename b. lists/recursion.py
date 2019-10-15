
'''
def print_hello():
    for i in range(0,10):
        print("hello world")

print_hello()

'''

def print_hello(i):
    #stopping condition
    if i == 0:
        return
    print("hello world")
    print_hello(i-1) # here it's then calling itself again. So the first time the function is run it prints with i = 9, and then it calls itself with i = 8

#once i = 0, the functions that have been created (all 10 of them) are then returned.
# But they're returned in reverse order, because they're calling each other back in the same chain they were created

# on first iteration is called i-1 (9), and then passes i-1 onto the next recursion - i-1 = 8, and so on
print_hello(10)

#NB recursion takes up memory quickly, because it's storing each instance separately