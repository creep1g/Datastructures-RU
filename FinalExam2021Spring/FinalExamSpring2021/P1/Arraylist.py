class Arraylist:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.arr = [None] * self.capacity

    def is_sorted_asc(self):
        if self.size == 0:
            return True

        return self.is_sorted_recur(self.arr)

    def is_sorted_recur(self, arr):
        '''Recursively walk through array comparing current 1st index to the
        element in 0+1 index, if element at arr[0] is not less than arr[0+1]
        return False'''
        if arr[0+1] is None:
            return True
        
        if arr[0] <= arr[0+1]:
            return self.is_sorted_recur(arr[1:])
        else:
            return False

    def in_range(self, index_low, index_high, val_low, val_high):
        
        return self.in_range_recur(index_low, index_high, val_low, val_high)
        

    def in_range_recur(self, start, end, low, high):
        '''Recursively walks through list and check if value at arr[start], is
        less than or equal to high and greater than or equal to low. if this
        case is broken we return False''' 
        if start > end:
            return True
        
        if high >= self.arr[start] >= low:
            return self.in_range_recur(start+1, end, low, high)
        else:
            return False


    def append(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    def resize(self):
        if not self.size >= self.capacity:
            return
        self.capacity *= 2
        tempArr = [None] * self.capacity
        for i in range(self.size):
            tempArr[i] = self.arr[i]
        self.arr = tempArr

    def __str__(self):
        ret_str = ""
        for i in range(self.size):
            ret_str += str(self.arr[i]) + " "
        return ret_str

if __name__ == "__main__":
    lis = Arraylist()
    lis.append(1)
    lis.append(2)
    lis.append(3)
    lis.append(4)
    print(lis)
    print("sorted: " + str(lis.is_sorted_asc()))
    print("in_range index 1-3, value 0-100... " + str(lis.in_range(1,3,0,100)))

    lis = Arraylist()
    lis.append(1)
    lis.append(2)
    lis.append(1)
    lis.append(4)
    print("")
    print(lis)
    print("sorted: " + str(lis.is_sorted_asc()))
    print("in_range index 1-3, value 1-3... " + str(lis.in_range(1,3,1,3)))
    
    lis = Arraylist()
    lis.append(1)
    lis.append(1)
    lis.append(1)
    lis.append(4)
    print("")
    print(lis)
    print("sorted: " + str(lis.is_sorted_asc()))
    print("in_range index 2-3, value 2-4... " + str(lis.in_range(2,3,2,4)))

    lis = Arraylist()
    lis.append(1)
    lis.append(1)
    lis.append(1)
    lis.append(4)
    lis.append(5)
    lis.append(5)
    lis.append(6)
    lis.append(50)
    lis.append(51)
    print("")
    print(lis)
    print("sorted: " + str(lis.is_sorted_asc()))
    print("in_range index 4-7, value 5-50... " + str(lis.in_range(4,7,5,50)))

    lis = Arraylist()
    lis.append(1)
    lis.append(1)
    lis.append(1)
    lis.append(0)
    print("")
    print(lis)
    print("sorted: " + str(lis.is_sorted_asc()))
    print("in_range index 0-2, value 1-1... " + str(lis.in_range(0,2,1,1)))
