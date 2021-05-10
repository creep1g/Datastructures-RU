import random
#  To testn
import math

class MyHashableKey:

    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return (self.int_value == other.int_value) and (self.string_value ==
                other.string_value)

    def __hash__(self):

        string_int = 0
        last_char = chr(1)
        offset = 31
        
         #  Use offset to help make string int more unique for each
         #  string since 'alfred' and 'falder' would generate the same integer
         #  value
        for char in self.string_value:
            string_int += ord(char) * pow(offset, ord(last_char))
            last_char = char
            offset += 1

        return string_int * self.int_value


if __name__ == "__main__":
    arr = [0] * 16

    for i in range(200):
        test_str = ""
        for i in range(14):
            test_str += chr(random.randint(65, 122))
        test_test = random.randint(1, 100)
        key = MyHashableKey(test_test, test_str)
        index = hash(key)%16
        arr[index] += 1
    print(arr)


