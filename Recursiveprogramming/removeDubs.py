from linearSearch import linearSearch
# Remove duplicates
# takes a list as parameter, returns another list
# list with all the same values but only one instance of each

def findDups(arr):
    
    new_arr = []
    
    if arr == []:
        new_list = []
    
    else: 
        if arr[0] not in arr[1:]:
            new_arr = [arr[0]] + findDups(arr[1:])
    
        else:
            new_arr = findDups(arr[1:])
    
    return new_arr

if __name__ == '__main__':
    arr = [1, 1, 3, 2, 6, 6, 78, 8, 1, 8]
    print(sorted(findDups(arr)))


