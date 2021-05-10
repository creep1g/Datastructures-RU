from linearSearch import linearSearch
# Duplicates in a list
# Implement a recursive functin that checks for duplicate values ina rlist
# takes a list as parameter
# Returns boolean value
#   True if any value in the list appears more than once otherwise False

def findDups(arr):
    if not arr:
        return False

    if len(arr) > 0:
        if linearSearch(arr[1:], 0, len(arr)-2, arr[0]):
            return True
    
    return findDups(arr[1:])

if __name__ == '__main__':
    arr = [0, 9, 3, 4, 5, 6, 78, 8, 1, 8]
    print(findDups(arr))


