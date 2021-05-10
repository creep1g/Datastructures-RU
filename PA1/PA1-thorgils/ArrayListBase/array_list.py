class IndexOutOfBounds(Exception):
    pass


class Empty(Exception):
    pass


class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

    # Time complexity: O(n) - linear time in size of list
    def __str__(self):
        '''Create a comma + space seperated string of array elements'''
        return_string = ""
        for i in range(self.size):
            if i+1 < self.size:
                return_string += "{}, ".format(self.arr[i])
            else:
                return_string += str(self.arr[i])  # No comma on last index
        return return_string

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        '''Adds value to arr[0] by shuffling every index to the right by one
        index. If array is at capacity resize it and call this functiion again
        recursively'''
        if self.size < self.capacity:
            for i in range(self.size, 0, -1):
                self.arr[i] = self.arr[i-1]
            self.arr[0] = value
            self.size += 1
        else:
            self.resize()
            self.prepend(value)

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        '''Inserts a value at a givien index by moving each item fro given
        index to the right'''
        if index > self.size or index < 0:
            raise IndexOutOfBounds

        if self.size < self.capacity:
            for i in range(self.size, index, -1):
                self.arr[i] = self.arr[i-1]
            self.arr[index] = value
            self.size += 1
        else:
            self.resize()
            self.insert(value, index)

    # Time complexity: O(1) - constant time
    def append(self, value):
        '''Adds value to the last index of the array if array is at capacity
        resize it and call this function recursively'''
        if self.size < self.capacity:
            self.arr[self.size] = value
            self.size += 1
        else:
            self.resize()
            self.append(value)

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        '''Set value of index to new value'''
        if index > self.size - 1 or index < 0:
            raise IndexOutOfBounds
        else:
            self.arr[index] = value

    # Time complexity: O(1) - constant time
    def get_first(self):
        '''Returns first element of array'''
        if self.size == 0:
            raise Empty
        return self.arr[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        '''Returns value of index'''
        if index > self.size - 1 or index < 0:
            raise IndexOutOfBounds
        else:
            return self.arr[index]

    # Time complexity: O(1) - constant time
    def get_last(self):
        '''Returns last value of array'''
        if self.size == 0:
            raise Empty
        return self.arr[self.size - 1]

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        '''Adds *2 indecies to array'''
        temp = self.arr
        temp_cap = self.capacity
        temp_size = self.size
        self.clear()
        self.capacity = temp_cap * 2
        self.size = temp_size
        self.arr = [0] * self.capacity
        for i in range(self.size):
            self.arr[i] = temp[i]

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        '''Removes element at given index'''
        if index > self.size - 1 or index < 0:
            raise IndexOutOfBounds
        else:
            for i in range(index, self.size - 1):
                self.arr[i] = self.arr[i+1]
            self.size -= 1

    # Time complexity: O(1) - constant time
    def clear(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

    # Time complexity: O(n) - linear time in size of sublist
    def sublist(self, start, length):
        if start + length > self.size or start < 0:
            raise IndexOutOfBounds
        else:
            ret_arr = ArrayList()
            for i in range(start, length+start):
                ret_arr.append(self.arr[i])
            return ret_arr

    # Time complexity: O(n) - linear time in size of concatinated list
    # OR
    # Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        '''Concatenates two arrays'''
    
        ret_arr = ArrayList()
        for i in range(self.size + other.size):
            if ret_arr.size < self.size:
                ret_arr.append(self.get_at(i))
            else:
                ret_arr.append(other.get_at(i - self.size))
        return ret_arr

if __name__ == "__main__":
        # add your tests here or in a different file.
        # Do not add them outside this if statement
        # and make sure they are at this indent level

        arr_lis = ArrayList()
        assert arr_lis.__str__() == ""
        for i in range(4):
            arr_lis.append(i)

        assert arr_lis.__str__() == "0, 1, 2, 3"

        for i in range(8):
            arr_lis.append(i)

        arr_lis.prepend(22)
        print(arr_lis)
        assert arr_lis.__str__() == "22, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7"
        assert arr_lis.get_first() == 22
        assert arr_lis.get_last() == 7

        arr_lis.insert(99, 4)

        assert arr_lis.get_at(4) == 99
        assert arr_lis.__str__() == "22, 0, 1, 2, 99, 3, 0, 1, 2, 3, 4, 5, 6, 7"   
        arr_lis.remove_at(4)
        assert arr_lis.__str__() == "22, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7"
        arr_lis.set_at(33, 1)
        assert arr_lis.__str__() == "22, 33, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7"
        new_list = ArrayList()
        arr_lis.clear()
        assert arr_lis.__str__() == ""
        for i in range(5):
            new_list.append(i)
            arr_lis.append(i)
        print(arr_lis)
        print(new_list)
        temp_list = arr_lis.concatenate(new_list)
    
        assert temp_list.__str__() == "0, 1, 2, 3, 4, 0, 1, 2, 3, 4"
        print(new_list)
        print(arr_lis)
        print(temp_list)
        print(arr_lis.size)
        print(arr_lis.sublist(1, 4))
