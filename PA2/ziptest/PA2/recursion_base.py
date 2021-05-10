class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    '''Recursively walks through linked list and prints out each elment'''
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def get_size(head):
    '''Returns a count of elements in LL'''
    if not head:
        return 0
    else:
        return 1 + get_size(head.next)

def reverse_list(head):
    '''Reverses linked list'''
    if not head or not head.next:  # If we are at the last element return head
        return head
    else:
        rev_head = reverse_list(head.next) # recursively call reverse list with
        # next node
        head.next.next = head  # On the way back down the call stack change
        # head's next and next-next.
        head.next = None
        return rev_head

def palindrome(head):
    '''Accepts head of linked list returns True if list is a palindrome, Else
    it returns False'''
    size = get_size(head)
    if size == 0:  # If list is empty it must be a palindrome
        return True
    new_head = node_copy(head)
    rev_head = reverse_list(new_head)
    is_palindrome = palindrome_helper(head, rev_head)
    del rev_head  #  Delete this instance of Node
    return is_palindrome


def node_copy(head):
    '''Generates an exact copy of given list'''
    if not head:
        return None
    else:
        new_node = Node(head.data, node_copy(head.next))
        return new_node

def palindrome_helper(head, rev_head):
    '''Checks if '''
    if not head:  # If we are no longer within the list, we have sucessfully
        # Walked the whole list return true
        return True
    else:
        if head.data == rev_head.data:
            # While both sides are the same keep calling this function
            return palindrome_helper(head.next, rev_head.next)
        else:
            # If we find a mismatch of elements, return False and stop the
            # recursion
            return False


if __name__ == "__main__":
    ##
    print("GET_SIZE TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = None
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", None)
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", Node("C", None))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)


    ##
    print("REVERSE TESTS")
    print("\n")
    head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)
    print_to_screen(head)
    print("\n")
    head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", None)
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = None
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", None))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)


    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
