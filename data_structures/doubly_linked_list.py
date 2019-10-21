class Node:
    def __init__(self, node_value):
        self._node_value = node_value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    
    def __init__(self):
        self._first = None

        
    def insert_front(self, node_value):
        if self._first is None:
            new_node = Node(node_value)  # pass an item to a new node
            new_node.previous_node = None
            self._first = new_node  #one node in array, so first = tail

        else:
            new_node = Node(node_value)
            current_node = self._first
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node
            new_node.previous_node = current_node
            new_node.next_node = None
            self._first = new_node


    def insert_back(self):
        pass
        
    def pop_front(self):
        if self._first is not None:
            previous_first = self._first
            self._first = self._first.next_node
            return previous_first

    def pop_back(self):
        pass

    def __iter__(self):
        current = self._first
        while current:
            yield(current.node_value)

    def print_list(self):
        current = self._first
        while current.next_node:
            print(self._first)
            current = current.next_node

    def __len__(self, length):
        current_node = self._first
        count = 0
        if self._first is None:
            return 0
        else:
            while current_node.next is not None:
                current_node = current_node.next
                count += 1
            return count

testlist = DoublyLinkedList()

testlist.insert_front(12)
testlist.insert_front(14)
print(testlist.__iter__())
print(testlist.print_list())


