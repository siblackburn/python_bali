import timeit
import time

def my_function():
    for i in range(10000):
        pass
    return

timing = timeit.timeit(
    lambda: my_function(),

    # number of times to execute your function
    # this is done to increase the accuracy of
    # measurement
    number=10000
)
print(f'avg milliseconds: {timing}')