import time

def decorator_try(func):
    def wrapper(x, n):
        count = 0
        while count < n:
            try:
                func(x)
            except Exception:
                print(f'test has failed {count + 1} times')

            count += 1
    return wrapper

@decorator_try
def time_function(x, n):
    print('Executing original function')
    time.sleep(x)

    return f'this doesnt work'

timer = 2
number_of_tries = 5
test = time_function(timer, number_of_tries)
print(test)