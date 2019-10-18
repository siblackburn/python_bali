class Node:
    def __init__(self, node_value=None, next = None): #by default the first node won't have anything to point to, so should be none
        self._node_value = node_value
        self.next_node = next

    def __repr__(self):
        return f'Node, value of {self._node_value} points to {self.next_node}'


class LinkedList:
    
    def __init__(self):
        self._first = None
        self.count = 0

    '''
    Complexity: O(1) because this is only ever dealing with 2 items in the linked list
    '''

    def __repr__(self):
        return f"Linked list starting with {self._first}"

    def __contains__(self, key):
        if self._first is None:
            return False
        else:
            current_node = self._first
            while current_node is not None:
                if current_node._node_value == key:
                    return True
                current_node = current_node.next
            return False

    def __iter__(self):
        current = self._first
        while current:
            yield(current.node_value)

    # Complexity: O(n)
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

    def insert_front(self, item):
        new_node = Node(item) #pass an item to a new node
        new_node.next = self._first # make the previous first item the second node (using .next)
        self._first = new_node #make the new item the first node

    '''
    # function to remove the first item
    # Complexity: O(
    '''

    def pop_front(self):
        if self._first is not None:
            previous_first = self._first
            self._first = self._first.next
            return previous_first

    '''
    # remove all instances of an object
    # Complexity: O(n) because it will sort through the entire list once, regardless of whether key is found
    '''

    def delete_item(self, key):
        if self._first == key:
            self._first = self._first.next
        current_node = self._first
        previous_node = None # creating an empty object of previous node, which then moves forward with current node
        while current_node is not None:
            if current_node == key:
                previous_node.next = current_node.next # the node link from previous node is now replacing the current node link
            previous_node = current_node  # move the previous node forward
            current_node = current_node.next # move the current node forward

    '''
    Function to find a key and remove the first instance from it. 
    while loop ensures that we loop through until we either reach the end of the list, or we find the key
    '''
    def delete_first_key(self, key):
        current = self._first
        previous = None

        if current == key:
            self._first = self._first.next
            return
        while current and current == key:
            previous = current
            current = current.next
        if current is None:
            return

        previous.next = current.next

    '''
    Reverses the Linked list, meaning the first item is now the last. 
    Defines previous node and current node (0 and head)
    then pushes each element backward in the queue one by one
    '''
    def reverse_list(self):
        previous_node = None
        current_node = self._first
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self._first = previous_node


'''
Quick test to see if reverse function works as it should
'''
testlist = LinkedList()
testlist.insert_front(12)
testlist.insert_front(13)
testlist.insert_front(14)
testlist.insert_front(15)

print(testlist)

testlist.reverse_list()
print(testlist)











