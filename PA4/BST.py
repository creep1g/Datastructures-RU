class MyComparableKey:

    def __init__(self, int_value, str_value):
        self.int_value = int_value
        self.str_value = str_value

    def __lt__(self, other):
        '''Compares two instances of MyComparableKey'''
        if self.int_value == other.int_value:
            return self.str_value < other.str_value
        else:
            return self.int_value < other.int_value

class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class BSTMap:

    class Node:

        def __init__(self, key=None, val=None, right=None, left=None):
            '''Initializes new node with a Key:Value pair and pointers to Left
            and Right Nodes'''
            self.key = key
            self.val = val
            self.right = right
            self.left = left

        def __str__(self):
            return '{' + str(self.key) + ':' + str(self.val) + '}'

    def __init__(self):
        '''Initializes Tree with a root'''
        self.root = None

    def __get_node(self, node, key):
        '''Returns the instance of node containing given key'''
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self.__get_node(node.left, key)

        elif key > node.key:
            return self.__get_node(node.right, key)

    def insert(self, key, data):
        '''Adds new node to the BT, making sure to keep it ordered'''

        if not self.root:
            self.root = self.Node(key=key, val=data)

        else:
            if self.__get_node(self.root, key):
                raise ItemExistsException()

            self.__insert_helper(key, data, self.root)

    def __insert_helper(self, key, data, node):
        '''Recursively walks tree finding the appropriet node to connect to'''
        if key > node.key:
            if not node.right:
                node.right = self.Node(key=key, val=data)

            else:
                self.__insert_helper(key, data, node.right)

        elif key < node.key:
            if not node.left:
                node.left = self.Node(key=key, val=data)

            else:
                self.__insert_helper(key, data, node.left)

    def find(self, key):
        '''Returns data value from key'''

        node = self.__get_node(self.root, key)

        if not node:
            raise NotFoundException()

        else:
            return node.val

    def contains(self, key):
        '''Returns True if key is present in tree, else return False'''
        if not self.__get_node(self.root, key):
            return False

        else:
            return True

    def update(self, key, data):
        '''Sets value of value pair with equal key to data'''
        node = self.__get_node(self.root, key)
        if not node:
            raise NotFoundException()

        else:
            node.val = data

    def remove(self, key):
        '''Removes value pair with equal key from the collection'''
        node = self.__get_node(self.root, key)

        if not node:
            raise NotFoundException()

        self.__rem_helper(self.root, key)

    def __rem_helper(self, node, key):
        '''Recursively walks tree and finds node with equal key.
            when key is found throw node to detatch function
        '''
        if node is None:
            return

        if node.key > key:
            node.left = self.__rem_helper(node.left, key)

        if key > node.key:
            node.right = self.__rem_helper(node.right, key)

        if node.key == key:
            node = self.__detatch_node(node)

        return node

    def __detatch_node(self, node):
        '''a'''
        if node.left is None and node.right is None:
            node = None
            return node

        if node.right is None:
            return node.left

        if node.left is None:
            return node.right

        leftmost = self.__leftmost(node.right)
        node.key = leftmost.key
        node.val = leftmost.val
        node.right = self.__rem_helper(node.right, leftmost.key)
        return node

    def __leftmost(self, node):
        '''Returns leftmost node'''
        if node.left is not None:
            return self.__leftmost(node.left)
        return node

    def __getitem__(self, key):
        '''Returns data from key value pair where key = key'''
        return self.find(key)

    def __setitem__(self, key, data):
        '''Sets value of key value pair where key = key to data.
            If key does not exist add new node
        '''
        node = self.__get_node(self.root, key)
        if not node:
            self.insert(key, data)

        else:
            self.update(key, data)

    def __len__(self):
        '''Returns the number of elements in the entire data structure'''
        return self.__len_helper(self.root)

    def __len_helper(self, node):
        '''Recursively walks through the tree and return its node count'''
        if node is None:
            return 0
        return (1 + self.__len_helper(node.left) +
                self.__len_helper(node.right))

    def __str__(self):
        '''Returns stringed version of the tree'''
        ret_str = self.__tree_str_recur(self.root, '')
        return ret_str

    def __tree_str_recur(self, node, string):
        '''Reursively walks through tree and appends each nodes key:value pair
        to a string inorder'''
        if node is None:
            return ""
        new_str = self.__tree_str_recur(node.left, string)
        new_str += str(node) + ' '
        new_str += self.__tree_str_recur(node.right, string)
        return new_str


if __name__ == '__main__':
    bst = BSTMap()
    bst[8] = 'eight'
    bst[10] = 'ten'
    bst[2] = 'two'
    bst[1] = 'one'
    bst[3] = 'three'
    bst[18] = 'eighteen'
    bst[12] = 'twelve'
    bst[9] = 'nine'
    bst[20] = 'twenty'
    bst[4] = 'four'
    bst[15] = 'fifteen'
    bst[7] = 'seven'
    print('Size', len(bst))
    print(bst)
    print('Remove 8')
    bst.remove(8)
    print(bst)
    print('Size', len(bst))
    print('Remove 4')
    bst.remove(4)
    print(bst)
    print('Size', len(bst))
    print('Remove 15')
    bst.remove(15)
    print(bst)
    print('Size', len(bst))
    print('Remove 20')
    bst.remove(20)
    print(bst)
    print('Size', len(bst))
    print('Remove 10')
    bst.remove(10)
    print(bst)
    print('Size', len(bst))
    print('Remove 9')
    bst.remove(9)
    print(bst)
    print('Size', len(bst))

    key1 = MyComparableKey(1, 'b')
    key1a = MyComparableKey(1, 'a')
    key2 = MyComparableKey(2, 'd')
    key8 = MyComparableKey(8, 'k')
    print(key1 < key1a)
    print(key1a < key1)
    print(key2 < key1a)
    print(key8 < key1a)
    print(key1 < key8)
    print(key1 < key2)
    print(key2 < key8)

