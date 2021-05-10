from DLL_class import _DoubleLinkedList

class Deque(_DoubleLinkedList):
    
    def add_front(self, data):
        self.insert_front(data)

    def add_back(self, data):
        self.insert_back(data)

    def get_last(self):
        return self.sentinel.prev.element

    def get_first(self):
        return self.sentinel.next.element

    def get_size(self):
        return self._size

    def print_reverse(self):
        node = self.sentinel.prev
        ret_str = ""
        while node is not self.sentinel:
            ret_str += "{} ".format(node.element)
            node = node.prev
        return ret_str

    def __str__(self):
        node = self.curr
        ret_str = ""
        while node is not self.sentinel:
            ret_str += "{} ".format(node.element)
            node = node.next
        return ret_str



if __name__ == '__main__':
    deq = Deque()
    deq.add_front(1)
    deq.add_front(2)
    deq.add_front(3)
    deq.add_front(4)
    deq.add_front(5)
    deq.add_front(6)
    deq.add_front(7)
    deq.add_front(8)
    deq.add_front(9)
    deq.add_back(10)
    deq.add_back(11)
    deq.add_back(12)
    deq.add_back(13)
    deq.add_back(14)
    deq.add_back(15)
    deq.add_back(16)
    print(deq)
    print(deq.pop_back())
    print(deq.pop_front())
    print(deq)
    print(deq.print_reverse())
    print(deq.get_first())
    print(deq.get_last())
    deq.add_back(3190)
    print(deq.get_size())
