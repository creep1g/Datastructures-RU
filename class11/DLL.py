class _DoublyLinkedBase:
    '''A base tclass porividing a doubly linked list representation.'''

    class _Node:
        '''Lightweight nonpublic class for storing a doubly linked node.'''
        __slots__ = '_element', '_prev', '_next'  # streamline Memory

        def __init__(self, element, prev, next):   # Initialize node's fields
            self._element = element               # user's element
            self._prev = prev                     # previous node reference
            self._next = next                     # next node reference

    def __init__(self):
        '''Create an empty list'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # Trailer is after header
        self._trailer._prev = self._header  # Header is before trailer
        self._size = 0                      # Number of elements

    def __len__(self):
        -'''Returns the number of elements in the list.'''
        return self._size

    def is_empty(self):
        '''Return True if list is empty.'''
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and return new node.'''
        newest = self._Node(e, predecessor, successor)  # Linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        '''Delete nonsentinel node from the list and return its element.'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # Record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element  # Return deleted element


class LinkedDeque(_DoublyLinkedBase):
    '''Double-ended queue implementation'''

    def first(self):
        '''Return (but do not remove) the element at the front of the deque.'''
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element  # Real item just after header

    def last(self):
        '''Return (bud do not remove) the element at the back of deque.'''
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element  # Real item just before trailer

    def insert_first(self, e):
        '''Add an element to the front of the deque.'''
        self.insert_between(e, self._header, self._header._next)  # After header

    def insert_last(self, e):
        '''Add element to the back of the deque.'''
        self._insert_between(e, self._traileer._prev, self._trailer)

    def delete_first(self):
        '''Remove and return the element from the front of the deque Raise
        empty exception if hte deque is empty'''

        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self.header.next) # Use inherited method

    def delete_last(self):
        '''Remove and return the element from th eback of the deque.
        Raise empty exception if the deque is empty'''
    if self.is_empty():
        raise Empty("Deque is empty"
                return self._delete_node(self._trailer._prev)  # use inheritd
