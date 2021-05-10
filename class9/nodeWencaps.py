class Linked:

    class _Node:
        def __init__(self, data=None, Next=None):
            self.data = data
            self.next = Next

    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, data):
        self.head = self._Node(data, self.head)
        self._size += 1
    
    def pop(self):
        if self.head != None:
            data = self.head.data
            self.head = self.head.next
            self._size -= 1
            return data
        else:
            return None

    def get_size(self):
        return self._size

    def __str__(self):
        ret_str = ''
        head = self.head
        while head != None:
            ret_str += str(head.data) + " "
            head = head.next
        return ret_str

if __name__ == '__main__':
    ll = Linked()
    ll.push(2) 
    ll.push(22) 
    ll.push(222) 
    ll.push(13) 
    ll.push(49)
    print(ll.get_size())
    print(ll)
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
    
    print(ll.get_size())
