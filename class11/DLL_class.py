from DLL_node import Node


class _DoubleLinkedList:

    def __init__(self):
        self.sentinel = Node()
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
        self.curr = self.sentinel
        self._size = 0

    def insert_front(self, element):
        '''Insert element to an arbritary location in the list
        If index > size raise index out of bounds'''

        node = Node(element)

        node.prev = self.curr.prev
        node.next = self.curr
        self.curr.prev.next = node
        self.curr.prev = node
        self.curr = node
        self._size += 1

    def insert_back(self, element):
        node = Node(element)
        node.prev = self.sentinel.prev
        node.next = self.sentinel
        self.sentinel.prev.next = node
        self.sentinel.prev = node
        self._size += 1

    def pop_front(self):
        if self.sentinel.next is self.sentinel:
            return None

        ret_node = self.sentinel.next
        ret_node.next.prev = self.sentinel
        self.sentinel.next = ret_node.next
        self.curr = self.curr.next
        self._size -= 1
        return ret_node.element

    def pop_back(self):
        if self.sentinel.next is self.sentinel:
            return None

        ret_node = self.sentinel.prev
        ret_node.prev.next = self.sentinel
        self.sentinel.prev = ret_node.prev
        self._size -= 1
        if self._size == 0:
            self.curr = self.sentinel

        return ret_node.element

    def __str__(self):
        '''Stringify list'''
        node = self.curr
        ret_str = ""
        while node != self.sentinel:
            ret_str += " {}".format(node.element)
            node = node.next
        return ret_str


if __name__ == '__main__':
    dll = _DoubleLinkedList()

    dll.insert_front(1)

    dll.insert_front(2)
    dll.insert_back(3)
    dll.insert_back(4)
    dll.insert_front(5)
    dll.insert_back(6)
    print(dll)
    print(dll.pop_back())
    print(dll)
    print(dll.pop_back())
    print(dll)
    print(dll.pop_back())
    print(dll)
    print(dll.pop_back())
    print("list",dll)
    print("pop",dll.pop_back())
    print(dll)
    print("pop",dll.pop_back())
    print("pop",dll.pop_back())
    print("pop",dll.pop_back())
    print("pop",dll.pop_back())
    print("pop",dll.pop_back())
    print(dll)
