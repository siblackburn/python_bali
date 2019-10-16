class Node:
    def __init__(self, node_value=None): #by default the first node won't have anything to point to, so should be none
        self._node_value = node_value
        self.next_node = None


class LinkedList:
    
    def __init__(self):
        self._first = None

    def insert_front(self, item):
        new_node = Node(item) #pass an item to a new node
        new_node.next = self._first # make the previous first item the second node (using .next)
        self._first = new_node #make the new item the first node

# function to remove the first item
    def pop_front(self):
        if self._first is not None:
            previous_node = self._first
            self._first = self._first.next
            return previous_node

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

    def printing_nodes(self):
        current_node = self._first
        while current_node.next is not None:
            print(current_node, end=" ")
            current_node = current_node.next




