class Node:
    def __init__(self, element=None, prev=None, Next=None):
        __slots__ = 'element', 'prev', 'Next'
        self.next = Next
        self.prev = prev
        self.element = element
