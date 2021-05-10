class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self._head = None
        self._size = 0

    def push_front(self, data):
        '''Adds elements to the "front" of a linked list'''
        self._head = Node(data, self._head)
        self._size += 1

    def pop_front(self):
        '''Removes and returns the element that was last pushed to front'''
        if not self._head:
            return None  # If list is empty return None

        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return data

    def push_back(self, data):
        '''Adds element to the back of a linked list'''
        if not self._head:
            self.push_front(data)  # If list is empty.

        else:
            node = self._head
            while node.next is not None:
                node = node.next
            node.next = Node(data, None)
            self._size += 1

    def pop_back(self):
        '''Removes and returns the last element of a linked list'''
        if not self._head:
            return None  # If list is empty return None
        if not self._head.next:
            data = self._head.data
            self._head = None
            self._size -= 1
            return data

        node = self._head
        while node.next.next is not None:
            node = node.next
        data = node.next.data
        node.next = None
        self._size -= 1
        return data

    def get_size(self):
        '''Returns an integer value that represents the amount of elements in a
        linked list'''
        return self._size

    def __str__(self):
        '''Stringfies a linked list'''
        if not self._head:
            return ""  # Returns empty string if list is empty

        ret_str = ""
        node = self._head
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


if __name__ == "__main__":
    ll = LinkedList()
    ll.push_back(3)
    ll.push_back(1)
    ll.push_back(6)
    ll.push_back(9)
    print(ll.get_size())
    print(ll)
    print(ll.pop_front())
    print(ll.pop_front())
    print(ll.get_size())
    print(ll)
    ll.push_front(11)
    ll.push_front(16)
    ll.push_front(13)
    print(ll.get_size())
    print(ll)
    print(ll.pop_front())
    print(ll.pop_front())
    print(ll.pop_back())
    print(ll.pop_back())
    print(ll.get_size())
    print(ll)
    print(ll.pop_back())
    print(ll.pop_front())
    print(ll.get_size())
    print(ll)

