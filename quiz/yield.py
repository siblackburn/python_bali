def single_generator():
    for i in range(1,10):
        yield i

#every time it calls next it will call the next item in the sequence
#in real world - can use this as a generator to create infinite lists until a condition is met
# Thunk - placeholder generator that is to be called later