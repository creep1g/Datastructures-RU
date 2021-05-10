'''Binary Search Tree'''


class Node:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.data)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.__add_helper(value, self.root)

    def __add_helper(self, value, node):
        if value > node.data:
            if not node.right:
                node.right = Node(value)
            else:
                self.__add_helper(value, node.right)
        elif value < node.data:
            if not node.left:
                node.left = Node(value)
            else:
                self.__add_helper(value, node.left)
        return

    def contains(self, value):
        node = self.root
        while node is not None:

            if value < node.data:
                node = node.left
            elif value > node.data:
                node = node.right

            if node.data == value:
                return True
        else:
            return False
        return node

    def __len__(self):
        length = self.__len_helper(self.root)
        return length

    def __len_helper(self, node):
        if node is None:
            return 0
        else:
            return (1 + self.__len_helper(node.left) +
                    self.__len_helper(node.right))

    def __str__(self):
        ret_str = self.__tree_str_recur(self.root, "")
        return ret_str

    def __tree_str_recur(self, node, string):
        if node is None:
            return ""

        new_str = self.__tree_str_recur(node.left, string)
        new_str += str(node.data) + " "
        new_str += self.__tree_str_recur(node.right, string)
        return new_str


bst = BinarySearchTree()
bst.add(1)
bst.add(9)
bst.add(2)
bst.add(30)
bst.add(21)
bst.add(3)
bst.add(29)
bst.add(7)
bst.add(29)
bst.add(10)
print(bst)
print(len(bst))

