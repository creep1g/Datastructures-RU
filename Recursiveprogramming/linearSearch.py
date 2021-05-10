import random
# Linear search
# Imglement a recursive function that searches for a valaue in a list
# Takes a list and a single value as parameteres
# Returns boolean value
    # True if the value is in the list

def linearSearch(array, start, length,  element):
    if length < start:
        return False
    if array[start] == element:
        return True
    if array[length] == element:
        return True
    return linearSearch(array, start+1, length-1, element)

if __name__ == '__main__':
    array = [random.randint(1, 400) for i in range(100)]
    length = len(array)
    print(linearSearch(array, 0, length-1, 89))
    print(array)
