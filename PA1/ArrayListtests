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
        index. If array is at capacity resize it and call this function again
        recursively'''
        if self.size < self.capacity:
            for i in range(self.size, 0, -1):  # Reverse the range
                self.arr[i] = self.arr[i-1]
            self.size += 1
            self.arr[0] = value
        else:
            self.resize()
            self.prepend(value)

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        '''Insert value at a given index by moving items'''
        if index > self.size - 1:
            raise IndexOutOfBounds()
            return

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
        '''Adds value to the last index of the the array, if array is at
        capacity resize it and call this function recursively'''
        if self.size < self.capacity:
            self.arr[self.size] = value
            self.size += 1

        else:
            self.resize()
            self.append(value)

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index > self.size:
            raise IndexOutOfBounds
        self.arr[index] = value

    # Time complexity: O(1) - constant time
    def get_first(self):
        '''Return first index of arr'''
        return self.arr[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        '''Returns the value of arr[index] if index > size raise error'''
        if index > self.size - 1:
            raise IndexOutOfBounds()
        else:
            return self.arr[index]

    # Time complexity: O(1) - constant time
    def get_last(self):
        return self.arr[self.size - 1]

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        '''Adds 4 new spaces in memory'''
        self.capacity *= 2
        temp = self.arr
        self.arr = [0] * self.capacity

        for i in range(self.size):
            self.arr[i] = temp[i]

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        '''Removes element at given index by assigning arr[i+1] to arr[i]'''
        if index > self.size - 1:
            raise IndexOutOfBounds
        for i in range(index, self.size):

            self.arr[i] = self.arr[i+1]
        self.size -= 1

    # Time complexity: O(1) - constant time
    def clear(self):
        '''Removes every element of the array by generating a new empty
        array'''
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

    # Time complexity: O(n) - linear time in size of sublist
    def sublist(self, start, length):
        ret_arr = ArrayList()
        for i in range(3, 5):
            ret_arr.append(self.arr[i])
        return ret_arr

    # Time complexity: O(n) - linear time in size of concatinated list
    # OR
    # Time complexity: O(n+m) -
    # linear time in size of both lists, self and other
    def concatenate(self, other):
        '''Concatenate two arrays'''
        cat_size = self.size + other.size
        temp = self.arr
        self.clear()
        self.__cat_helper(temp, self.size)
        self.__cat_helper(other, other.size)
        self.size = cat_size

    def __cat_helper(self, list_in, size):
        for i in range(size):
            self.append(list_in[i])


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

    assert arr_lis.__str__() == "22, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7"
    assert arr_lis.get_first() == 22
    assert arr_lis.get_last() == 7

    arr_lis.insert(99, 4)

    assert arr_lis.get_at(4) == 99
    print(arr_lis)
    print(arr_lis.size)
    arr_lis.remove_at(13)
    print(arr_lis)
    arr_lis.set_at(13, 2)
    print(arr_lis)
    # assert arr_lis.__str__() == "22, 0, 1, 2, 99, 3, 0, 1, 2, 3, 4, 5, 6, 7"
    # arr_lis.remove_at(4)
    # print(arr_lis)
    # # assert arr_lis.__str__() == "22, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7"
    # arr_lis.set_at(33, 12)
    # assert arr_lis.__str__() == "22, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 33"
    # new_list = ArrayList()
    # arr_lis.clear()
    # assert arr_lis.__str__() == ""
    # for i in range(5):
    #     new_list.append(i)
    #     arr_lis.append(i)
    # arr_lis.append(new_list)
    # assert arr_lis.__str__() == "0, 1, 2, 3, 4, 0, 1, 2, 3, 4"
    # print(arr_lis)
    # print(arr_lis.sublist(4,3))
