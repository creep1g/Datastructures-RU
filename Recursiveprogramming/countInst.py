import random

# Implement a recursive funtin that countr a specific value in a list
# takes alist and a single value as parameters
# returns an integer value
# How many times does the value appear in the list?

def count_inst(array, element):
    if not array:
        return 0

    if array[0] == element:
        return 1 + count_inst(array[1:], element)

    else:
        return 0 + count_inst(array[1:], element)


if __name__ == '__main__':
    
    
    arr = [random.randint(1, 100) for i in range(998)]
    print(count_inst(arr, 50))
