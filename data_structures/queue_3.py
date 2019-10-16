from data_structures.stack import Stack


class QueueStack:

    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()

    def enqueue(self, item):
        """Add item to the enqueue stack.

        Parameters:
        item: item to add to the queue
        """
        while len(self._stack1) > 0:
            self._stack2.push(self._stack1.pop())
        self._stack2.push(item)

    def dequeue(self):
        """Remove item from the queue.

        Returns:
        item: First item in queue
        """
        while len(self._stack2) > 0:
            self._stack1.push(self._stack2.pop())
        return self._stack1.pop()


myqueue = QueueStack()
myqueue.enqueue("Hooray1")
myqueue.enqueue("Hooray2")
print(myqueue.dequeue())