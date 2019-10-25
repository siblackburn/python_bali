import time

def timed(seconds=False):
    count = 0
    def inner_decorator(func):
        def new_function(*args, **kwargs):
            start = time.time()
            count += 1
            func(*args, **kwargs)
            end = time.time()
            if seconds:
                print(f'my_f took: {end-start} seconds')
            else:
                print(f'my_f took: {(end-start)*1000} milliseconds')
        return new_function
    return inner_decorator


@timed(seconds=False)
def my_f(n, message):
    print(f'Executing my_f with {n} seconds: {message}')
    time.sleep(n)
    print('Done Executing my_f')


my_f(3, 'hello')