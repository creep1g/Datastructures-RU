
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        '''Initializes list with a single sentinel node that acts as Head and
        Trailer, initializes our current variable and sets its value to
        sentinel'''
        self._sentinel = Node()
        self.curr = self._sentinel
        self.curr.next = self._sentinel
        self.curr.prev = self._sentinel
        self._size = 0

    def insert(self, data):
        '''inserts value in front of current node'''
        node = Node(data=data)      # Creates new node containing users data
        node.prev = self.curr.prev  # Connects node to current's prev
        node.next = self.curr       # Connects node to current node
        self.curr.prev.next = node  # Connect the node left ofcurrent to new node
        self.curr.prev = node       # Connect current to new node
        self.curr = node            # Assign node to our current pointer
        self._size += 1             # Increase size

    def remove(self):
        '''Removes node at self.curr'''
        if self.curr == self._sentinel:
            return
        new_curr = self.curr.next   # Temp variable for node next of current
        prev_curr = self.curr.prev  # Temp variable for node previous to current
        prev_curr.next = new_curr   # Connect node before to node after
        new_curr.prev = prev_curr   # Connect node after to node before
        self.curr = new_curr        # Assign node after to current pointer
        self._size -= 1             # Decrease size

    def get_value(self):
        '''Returns current value'''
        return self.curr.data

    def move_to_next(self):
        '''Moves current pointer to next node to the "Right"'''
        if (self.curr.next != self._sentinel and self.curr.next !=
                self._sentinel.next):
            self.curr = self.curr.next
        else:
            self.curr = self._sentinel

    def move_to_prev(self):
        '''Moves current pointer to next node to the "left" '''
        if (self.curr.prev != self._sentinel):
            self.curr = self.curr.prev

    def move_to_pos(self, pos):
        '''Moves current pointer to a certain position in the list'''
        if pos > self._size or pos < 0:  # Does nothing if pos is out of range
            return

        node = self.get_first_node()
        for i in range(pos):
            node = node.next
        self.curr = node

    def clear(self):
        '''Deletes all nodes except sentinel'''
        node = self.get_first_node()
        temp = None
        while node != self._sentinel:
            temp = node.next  # Keep next node in a temp variable
            node.prev = None  # Disconnect node's previous
            node.next = None  # Disconnect node's next
            node.data = None  # Remove node's data
            del node          # Deletes instance of node
            node = temp       # Assign our temp noed to node
        self.curr = self._sentinel       # Make sure curr is at head
        self._sentinel.next = self.curr  # Make sure head points at curr
        self._sentinel.prev = self.curr  # Make sure tail points at curr
        self._size = 0                   # Reset sizet

    def get_first_node(self):
        '''Returns the first node of the list'''
        return self._sentinel.next

    def get_last_node(self):
        '''Returns the last node of the list'''
        return self._sentinel.prev

    def partition(self, low, high):
        '''Partitions list from low to high, uses low as a pivot, any node that
        contains data that is less than low is moved to the "left" of the node
        otherwise they remain on its right side.'''
        node = low.next
        temp = None

        while node != self._sentinel:
            if node.data < low.data:
                temp = node.next       # Keep next node in temp
                temp.prev = node.prev  # Give temp nodes prev to current prev
                node.prev.next = temp  # Disconnect curr.prev from node
                low.prev.next = node   # Connect the node before low to node
                node.prev = low.prev   # Connect lows prerv to inserted node
                low.prev = node        # Make inserted node low's previous
                node.next = low        # Make inserted node's next low
                node = temp            # Insert next node into node for loop
            else:
                node = node.next       # If data >= low's data do nothing

        self.curr = low                # Curr should point at pivot after

    def sort(self):
        '''Sorts list using _quicksort function'''
        start = self.get_first_node()  # Get first element of list
        end = self.get_last_node()     # Assign last node to end
        self._quicksort(start, end)
        self.curr = self.get_first_node()  # First node is now current

    def _quicksort(self, start, end, temp=None):
        '''Recursively sorts elements of list using partition'''
        if start != self._sentinel and end.next != start:
            #  Make sure start does not point to trailer node and end's next
            #  does not point to our starting node.
            self.partition(start, end)  # Run list through partitioner
            # Call quicksort with end at a static position and move pivot to
            # the next node (to the 'right')
            self._quicksort(self.curr.next, end)
            # Call quicksort with start at a static position and move back pivot
            # to the previous node (to the 'left')
            self._quicksort(self.get_first_node(), self.curr.prev)

    def __len__(self):
        '''Returns the size of the list'''
        return self._size

    def __str__(self):
        '''Returns a string of elements represinting our list'''
        ret_str = ""
        node = self._sentinel.next
        while node != self._sentinel:
            ret_str += "{} ".format(node.data)
            node = node.next
        return ret_str


if __name__ == "__main__":
    # create tests here if you want
    dll = DLL()
    dll.insert(29)
    dll.insert(11)
    dll.insert(13)
    dll.insert(25)
    dll.insert(23)
    dll.insert(18)
    dll.insert(18)
    print(dll)
    dll.sort()
    assert str(dll) == "11 13 18 18 23 25 29 "
