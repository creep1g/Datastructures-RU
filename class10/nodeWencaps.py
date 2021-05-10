class Linked:

    class _Node:
        def __init__(self, data=None, Next=None):
            self.data = data
            self.next = Next

    def __init__(self):
        self.head = self._Node()
        self.size = 0

    def push(self, data):
        self.head = self._Node(data, self.head)
        self.size += 1
    
    def pop(self):
        if self.head != None:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        else:
            return None

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ''
        head = self.head
        while head != None:
            ret_str += str(head.data) + " "
            head = head.next
        return ret_str


def length(head):
    if not head:
        return 0
    else:
        return 1 + length(head.next)

def insert(head, data):
    if not head:
        head.data = data
    # if head <

if __name__ == '__main__':
    ll = Linked()
    # ll.push(1)
    # ll.push(2)
    # ll.push(3)
    # ll.push(6)
    # ll.push(7)
    # ll.push(8)
    ll.push(9)
    insert(ll.head, 22)
    print("Using length function:",length(ll.head))
    print(ll) 
