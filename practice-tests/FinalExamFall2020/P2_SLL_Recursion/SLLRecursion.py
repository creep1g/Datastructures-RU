class sll_node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

##########################   helper functions are encouraged in these problems   ##########################

def is_asc_desc_ordered(head):
    return __is_asc_helper(head, head.next) or __is_desc_helper(head, head.next)

def __is_asc_helper(head, next):

    if next.next is None:
        if head.value < next.value:
            return True
        else:
            return False

    if head.value <= next.value:
        return __is_asc_helper(head.next, head.next.next)
    else:
        return False

def __is_desc_helper(head, next):

    if next.next is None:
        if head.value > next.value:
            return True
        else:
            return False

    if head.value >= next.value:
        return __is_desc_helper(head.next, head.next.next)
    else:
        return False

def count_ascending_series(head):
    return __count_helper(head, head.next, 1)

def __count_helper(head, next, series):
    if next.next is None:
        if head.value > next.value:
            return series + 1
        else:
            return series

    if head.value > next.value:
        return __count_helper(head.next, head.next.next, series+1)

    if head.value <= next.value:
        return __count_helper(head.next, head.next.next, series)

if __name__ == "__main__":
    print("is_asc_desc_ordered tests:")
    test_head = sll_node(1, sll_node(2, sll_node(3, None))) #1,2,3
    print(is_asc_desc_ordered(test_head))
    test_head = sll_node(3, sll_node(2, sll_node(1, None))) #3,2,1
    print(is_asc_desc_ordered(test_head))
    test_head = sll_node(1, sll_node(3, sll_node(2, None))) #1,3,2
    print(is_asc_desc_ordered(test_head))

    print("\ncount_ascending_series tests:")
    test_head = sll_node(1, sll_node(2, sll_node(3, None))) #1,2,3
    print(count_ascending_series(test_head))
    test_head = sll_node(3, sll_node(2, sll_node(1, None))) #3,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(2, sll_node(3, sll_node(2, sll_node(3, sll_node(4, sll_node(2, sll_node(7, sll_node(8, None))))))))) #1,2,3,2,3,4,2,7,8
    print(count_ascending_series(test_head))
    test_head = sll_node(5, sll_node(4, sll_node(3, sll_node(2, sll_node(1, None))))) #5,4,3,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(1, sll_node(1, sll_node(2, sll_node(1, None))))) #1,1,1,2,1
    print(count_ascending_series(test_head))
