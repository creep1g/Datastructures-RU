# Length of string
# Implement a recursive function that calculates the length of a string
# returns a n integer +1

def str_len(str_in):
    '''Returns the length of string'''
    if str_in == "":
        return 0
    else:
        return 1 + str_len(str_in[1:])


# Linear search
# Imglement a recursive function that searches for a valaue in a list
# Takes a list and a single value as parameteres
# Returns boolean value
  # True if the value is in the list

def linearSearch(array, element):
    if array[0] == element:
        return True
    else:
        linearSearch(array[1:], element)

if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    n = str_len(array)
    print(n)
