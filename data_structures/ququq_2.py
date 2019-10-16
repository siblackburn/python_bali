from data_structures.stack import Stack


class Queue:

    def __init__(self):
        self._data_stack = Stack()
        self._utility_stack = Stack()

    def enqueue(self, item):
        if self._data_stack.__len__() < 1:
            self._data_stack.push(item)
            return
        for _ in range(self._data_stack.__len__()): # "_" instead of an i variable means you don't care about the variable (saves memory)
            popped_item = self._data_stack.pop()
            self._utility_stack.push(popped_item)
        self._data_stack.push(item)
        for _ in range(self._utility_stack.__len__()):
            self._data_stack.push(self._utility_stack.pop())
            #everything is on the data stack in the original order

    def dequeue(self):
        if self._data_stack.__len__() < 1:
            raise Exception("queue is empty")
        return self._data_stack.pop()
# pop removes the data item that's been there the longest, when in a queue


    # def __len__(self):
    #     return len(self._data_stack)



test = Queue()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
# test.dequeue()
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())