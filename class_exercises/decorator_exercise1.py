import time


def decorator_time(func):
    def wrapper(x): #this is a new  version of timed function, with additional functionality
        print('Executing the wrapper')
        start = time.time()
        func(x)
        end = time.time()
        print(f'Time elapsed: {end - start}')

    return wrapper


#@decorator_time
def time_function(x):
    print('Executing original function')
    time.sleep(x)


wrapper = decorator_time(time_function) # This is how we would call it without using the @decorator sugar
# because the wrapper is now a new function entirely, which decorates the original function (timed_function)
test_output = wrapper(3)

print(test_output)