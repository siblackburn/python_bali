import time

def decorator_time(func):
    def wrapper(x): #this is a new  version of timed function, with additional functionality. This also needs to take an argument in order to run the inner function( 3 lines down)
        print('Executing the wrapper')
        start = time.time()
        func(x)
        end = time.time()
        print(f'Time elapsed: {end - start}')

    return wrapper


def new_func(x):
    time.sleep(x)
    return f'a load of balls'

@decorator_time
def time_function(x):
    print('Executing original function')
    time.sleep(x)

    return f'this doesnt work'


# calling this is different to exercise 1 because the @decorator has already applied the decorator and wrapper to our original function
# so when we call the original function, it will automatically wrap!!!
test_output = time_function(3)

print(test_output)

returning_something = decorator_time(new_func(2))
print(returning_something)

'''
1) Define original function
2) define a decorator, and pass it the original function
3) within the decorator, make a wrapper function, which will effecitvely replace the original function with added functionality. This will need the variables that the original function had
4) the decorator function then needs to return the wrapper
5) Because the original function is decorated, when we call it, it will return the wrapper rather than the original function, rather than what the original function should have returned
'''