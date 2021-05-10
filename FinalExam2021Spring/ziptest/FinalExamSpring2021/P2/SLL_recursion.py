class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sum_of_even_or_even(head):
    return sum_even_recur(head, 0, 0)

def sum_even_recur(head, index, total):
    if head is None:
        return 0
    # Walk up list
    total = sum_even_recur(head.next, index+1, total)
    # Check if index or data fits specifications
    if head.data%2 == 0 or index%2 == 0:
        total += head.data # Sum data
        
    return total # Return the susm

def count_smaller_than_prev(head):
    return count_smaller_recur(head, 0, None)

def count_smaller_recur(head, counter, prev):
    # Stop algorithm when head.next is None
    if head is None:
        return counter
    # If prev is None move 1 index up
    if prev is None:
        counter = count_smaller_recur(head.next, counter, head)
    else:
        counter = count_smaller_recur(head.next, counter, head)
        # Walk list checking if head.data < prev.data
        if head.data < prev.data:
            counter += 1
        # Add to counter when specifications are met
    return counter

if __name__ == "__main__":
    print("sum of even or even test")
    head = SLL_Node(1, SLL_Node(3, SLL_Node(2, SLL_Node(4, SLL_Node(2, SLL_Node(1))))))
    print(sum_of_even_or_even(head))
    head = SLL_Node(1, SLL_Node(2, SLL_Node(1, SLL_Node(0, SLL_Node(1, SLL_Node(0))))))
    print(sum_of_even_or_even(head))
    head = SLL_Node(1, SLL_Node(6, SLL_Node(2, SLL_Node(4, SLL_Node(2, SLL_Node(13))))))
    print(sum_of_even_or_even(head))
    head = SLL_Node(1, SLL_Node(5, SLL_Node(0, SLL_Node(2, SLL_Node(13, SLL_Node(0))))))
    print(sum_of_even_or_even(head))

    print("count smaller than prev test")
    head = SLL_Node(1, SLL_Node(3, SLL_Node(2, SLL_Node(4, SLL_Node(2, SLL_Node(1))))))
    print(count_smaller_than_prev(head))
    head = SLL_Node(1, SLL_Node(2, SLL_Node(1, SLL_Node(0, SLL_Node(1, SLL_Node(0))))))
    print(count_smaller_than_prev(head))
    head = SLL_Node(1, SLL_Node(6, SLL_Node(2, SLL_Node(4, SLL_Node(2, SLL_Node(13))))))
    print(count_smaller_than_prev(head))
    head = SLL_Node(1, SLL_Node(5, SLL_Node(0, SLL_Node(2, SLL_Node(13, SLL_Node(0))))))
    print(count_smaller_than_prev(head))
