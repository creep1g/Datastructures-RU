# Implement binary search in an ordered list using recursive programming

def binarySearch(array, low, high, element):
    if high >= low:
        mid = high + low // 2
        if array[mid] == element:
            return True
    
        elif array[mid] > element:
            return binarySearch(array, low, mid - 1, element)
        
        else:
            return binarySearch(array, mid + 1, high, element)
    else:
        return False

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,18,20,30,32,33,34,35]
    print(binarySearch(array,0,len(array)-1, 17))
    # print(binarySearch(array,0,len(arrgay)-1, 17))
