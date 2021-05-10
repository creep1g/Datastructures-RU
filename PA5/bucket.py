class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class Bucket:

    class Node:
        def __init__(self, key, value, Next):
            self.key = key
            self.value = value
            self.next = Next

        def __eq__(self, other):
            if (self.key == other.key and self.value == other.value and
                    self.next == other.next):

                return True
            else:
                return False

        def __str__(self):
            return '{' + str(self.key) + ':' + str(self.value) + '}'

    def __init__(self):
        self._head = None
        self._size = 0

    def insert(self, key, data):
        '''Adds key:value pair to the bucket if equal key is already in the
        bucket raise Exception'''
        if not self.contains(key):
            self._head = self.Node(key, data, self._head)
            self._size += 1
        else:
            raise ItemExistsException()

    def update(self, key, data):
        '''Sets data value of pair with equal key to data
        If not found raise Exception'''
        if self.contains(key):
            node = self.__find_helper(self._head, key)
            node.value = data
        else:
            raise NotFoundException()

    def find(self, key):
        '''Returnsthe data value of a key value pair, If not found
        raise NotFoundException'''
        node = self.__find_helper(self._head, key)
        if node is None:
            raise NotFoundException()
        else:
            return node.value

    def __find_helper(self, node, key):
        if node is None:
            return None
        else:
            if node.key == key:
                return node
            else:
                return self.__find_helper(node.next, key)

    def contains(self, key):
        '''Returns true if key is found in the bucket else return false'''
        if self.__find_helper(self._head, key) is None:
            return False
        else:
            return True

    def remove(self, key):
        '''Removes the key:value pair with equal key if key is not found raise
        an Exception'''
        node = self.__find_helper(self._head, key)
        if node is None:
            raise NotFoundException()
        if node == self._head:
            self._head = self._head.next
        else:
            before = self.__find_before(self._head, node)
            before.next = node.next
            node = None
        self._size -= 1

    def __find_before(self, head, node):
        '''Returns node inserted after '''
        if head is None:
            return head
        if head.next == node:
            return head
        else:
            return self.__find_before(head.next, node)

    def __setitem__(self, key, data):
        '''If item with equal key exists: Update. Else insert'''
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        '''Returns item with equivalent key'''
        return self.find(key)
    
    def __iter__(self):
        '''Iterate over datastructre'''
        node = self._head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        '''Returns Length of datastructure'''
        return self._size

    def __str__(self):
        ret_str = ''
        node = self._head
        for i in range(self._size):
            ret_str += str(node) + " "
            node = node.next
        return ret_str


if __name__ == '__main__':
    bucket = Bucket()
    bucket.insert(1, ['a', 'b'])
    bucket.insert(2, ['a', 'b'])
    bucket.insert(3, ['a', 'b'])
    bucket.insert(4, ['a', 'b'])
    print(bucket)
    bucket.remove(4)
    print(bucket)
    bucket[4] = 'mamma mia'
    print(bucket[4])

