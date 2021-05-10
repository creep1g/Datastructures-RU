
def less_than(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    '''Recursively checks if a < b by calling it self with values a and b decreased 
       by one, if a == 0 before b returns True else returns False'''
    if a == 0:
        return True
    elif b == 0 or a == b:
        return False
    else:
        return less_than(a-1, b-1)


def length(array):
    '''Returns the length of an array'''
    if array == []:
        return 0
    else:
        return 1 + length(array[1:])


def linear_search(value, arr, start, length):
    '''If value is found in array, return True, else returns False'''
    if length < start or length == 0:
        return False
    if arr[start] == value:
        return True
    if arr[length-1] == value:
        return True
    return linear_search(value, arr, start+1, length-1)


def unique(arr):
    '''Calls define an empty array and calls unique_helper with user-defined array and
       function-defined array'''
    new_arr = []
    new_arr = unique_helper(arr, new_arr)
    return new_arr


def unique_helper(arr_first, arr_second):
    '''Helper for unique function, takes an empty list and user defined list and uses 
       linear_search to look for instances in program-defined list, returns a list of 
       unique elements in user-defined list'''
    if arr_first == []:
        return arr_second
    if linear_search(arr_first[0], arr_second, 0, length(arr_second) is False:
        arr_second.append(arr_first[0])
        unique_helper(arr_first[1:], arr_second)
    else:
        unique_helper(arr_first[1:], arr_second)
    return arr_second


# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!0

def test_less_than(num1, num2):
    if(less_than(num1, num2)):
        print(str(num1) + " is less than " + str(num2))
    else:
        print(str(num1) + " is NOT less than " + str(num2))

def test_unique(lis1):
    print(str(unique(lis1)) + " are the unique items in " + str(lis1))

def run_recursion_program():

    print("\nTESTING LESS THAN:\n")

    test_less_than(8, 3)
    test_less_than(2, 9)
    test_less_than(4, 17)
    test_less_than(11, 3)
    test_less_than(8, 2)
    test_less_than(8, 7)
    test_less_than(7, 8)
    test_less_than(6, 16)
    test_less_than(7, 7)

    print("\nTESTING UNIQUE:\n")

    test_unique(['a', 'f', 'd', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'b', 'f', 'g', 'a', 't', 'c', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['f', 'g', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
    test_unique(['t'])


if __name__ == "__main__":
    run_recursion_program()
