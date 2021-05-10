class Node:
    def __init__(self, data=None, head=None, Next=None):
        self.data = data
        self.head = self
        self.next = Next


def push_front(head, data):
    return Node(data=data, Next=head)


def print_list(head):
    if head is None:
        print("None")
    else:
        print(head.data, end=" ")
        print_list(head.next)


def remove(head):
    node = Node()
    if head.next is None:
        print("Empty")
    else:
        node.head = head.next
        node.next = head.next.next
    return node


def push_back(head, data):
    node = head

    while node.next is not None:
        node = node.next
    node.next = Node(data=data, head=node.next, Next=None)

def remove_back(head):
    node = head
    before = node
    while node.next is not None:
        before = node
        node = node.next
    before.next = None

newNode = Node(data="1")
newNode = push_front(newNode.head, 8)
newNode = push_front(newNode.head, 23)
newNode = push_front(newNode.head, 22)
newNode = push_front(newNode.head, 39)
newNode = push_front(newNode.head, 212)

print_list(newNode.head)

push_back(newNode.head, 90)
push_back(newNode.head, 92)
push_back(newNode.head, 93)

print_list(newNode.head)

remove_back(newNode.head)
print_list(newNode.head)
remove_back(newNode.head)
print_list(newNode.head)
remove_back(newNode.head)

print_list(newNode.head)
