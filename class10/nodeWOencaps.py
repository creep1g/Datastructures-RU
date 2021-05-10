class Node:
    def __init__(self, data=None, Next=None):
        self.data = data
        self.head = self
        self.next = Next


def push_front(head, data):
    return Node(data=data, Next=head)


def print_list(head):
    if head is None:
        print("")
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


def length(head):
    if not head:
        return 0
    else:
        return 1 + length(head.next)


def insert(head, data):
    if not head.next:
        head.next = Node(data)
    if head.data <= data and head.next.data > data:
        head.next = Node(data, head.next)
    else:
        insert(head.next, data)


def reverse(head):

    if head == None:
        return head
    if head.next == None:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head

def merge_lists(head1, head2):
    
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head1.next = merge_lists(head1.next, head2)
        return head1

    else:
        head2.next = merge_lists(head1, head2.next)
        return head2

    

newNode = Node(3, Node(6, Node(15, Node(16, Node(16, Node(20,None))))))
# for i in range(1, 20):
    # if i % 2 == 1 and i != 1:
        # newNode = Node(i, newNode)

scndNode = Node(1, Node(8, Node(10,None)))
# for i in range(1, 20):
    # if i % 2 == 0 and i != 2:
        # scndNode = Node(i, scndNode)


print_list(newNode)
print_list(scndNode)
merged = merge_lists(newNode.head, scndNode.head)
insert(merged, 9)
print_list(merged)
