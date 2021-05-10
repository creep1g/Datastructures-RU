
class Array:
    def __init__(self, arr, count):
        self.capacity = 4
        while self.capacity < count:
            self.capacity *= 2
        self.arr = [None] * self.capacity
        for i in range(count):
            self.arr[i] = arr[i]
        self.size = count

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        for i in range(self.size):
            ret_str += str(self.arr[i]) + " "
        return ret_str

    def contains(self, val):
        return self.__contains_recur(self.arr, val)

    def __contains_recur(self, arr, val):
        if arr[0] == val:
            return True
        if arr[0] is None:
            return False

        return self.__contains_recur(arr[1:], val)

    def remove_all(self, other):
        return self.__rem(other)

    def __rem(self, other):
        i = 0
        num_removed = 0
        while i < self.size:
            self.arr[i] = self.arr[i + num_removed]
            if other.contains(self.arr[i + num_removed]):
                num_removed += 1
                self.size -= 1
            else:
                i += 1
        return num_removed


        # self.size = self.size - count

        return count
                

if __name__ == "__main__":
    arr1 = Array([1, 4, 2, 6, 5, 4, 5, 5, 7, 8, 3, None, None, None, None, None], 11)
    print(arr1)
    print(len(arr1))
    print(arr1.contains(7))
    print(arr1.contains(9))
    removed_count = arr1.remove_all(Array([2, 5, 4, None], 3))
    print(removed_count)
    print(arr1)
    print(len(arr1))
