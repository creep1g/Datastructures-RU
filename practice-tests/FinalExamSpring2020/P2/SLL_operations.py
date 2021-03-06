
class SLL_Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# IMPLEMENT HERE

def is_doubled(head1, head2):
    
    if head1 is None:
        return True
    
    if head2 is None:
        return False

    if head1.data == head2.data:
        return is_doubled(head1.next, head2)
    else:
        if head1.next is None:
            return False
        return is_doubled(head1, head2.next)


if __name__ == "__main__":
    
    print("\n\nTESTING DOUBLED:\n")

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(7, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4)))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9)))
    print(is_doubled(head1, head2))
