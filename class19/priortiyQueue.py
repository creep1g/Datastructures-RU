class PriorityQueue:

    class HeapNode:
        def __init__(self, key=None, data=None, right=None, left=None,
                     parent=None):
            self.key = key
            self.data = data
            self.right = right
            self.left = left
            self.parent = parent

        def __str__(self):
            ret_str = "{"+str(self.key)+":"+str(value)+"}"
            return ret_str

    def __init__(self):
        self.root = None
        self.lastNode = None
        self.lastIn = None

    def insert(self, key, data):
        '''Insert'''
        if self.root is None:
            # If heap is empty start at root
            self.lastNode = self.root = self.HeapNode(data=data)
        elif (self.lastNode.parent is None and self.lastNode is
              self.lastNode.parent.left):
            # The last node is a left node so we now add its right sibling and
            # make that the last node
            self.last_node.parent.right = self.HeapNode(key=key, data=data,
                                                parent=self.lastNode.parent)
            self.lastNode = self.lastNode.parent.right

        else:
            # Go all the way up right side of subtree
            next_to_add = self.lastNode

            while (next_to_add is not self.root and next_to_add is
            next_to_add.paprent.right):
                # If we're not at the root, go one ug and one down to the right
                next_to_add = next_to_add.parent.right

                if next_to_add is not self.root:
                    next_to_add = next_to_add.parent.right

            # Go all the way down the left side of subtree

            while next_to_add.left != None:
                next_to_add = next_to_add.left
            
            next_to_add.left = self.HeapNode(key=key, data=data,
                                             parent=next_to_add )
        node = self.last_node
        while node.parent != None and node.key < node.parent.key:
            self.swap_values(node, node.parent)
            node = node.parent




    def __str__(self):
        ret_str = self.__str_recur(self.root)
        return ret_str

    def __str_recur(self, node):
        if node is None:
            return ""

        new_str = self.__str_recur(node.left)
        new_str += str(node) + ' '
        new_str += self.__str_recur(node.right)
        return new_str


