class BT_Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def populate_tree(self):
        self.root = self.populate_tree_recur("root", 0, "")
    
    # Returns a node or None 
    def populate_tree_recur(self, parent_name, level, left_right_string):
        data = ""
        if left_right_string == "":
            data = input("Enter the name of the root: ")
        else:
            data = input(("*" * level) + "Enter the name of the " +
                    left_right_string + " node with parent node " + parent_name
                    + ": ")

        if data == "":
            return None
        node = BT_Node(data)
        node.left = self.populate_tree_recur(data, level + 1, "Left ")
        node.right = self.populate_tree_recur(data, level + 1, "Right ")
        return node

    def print_tree(self):
        self.print_tree_recur(self.root)

    def print_tree_recur(self, node):
        if node == None:
            return
        
        # Pre
        print(node.data)
        self.print_tree_recur(node.left)
        self.print_tree_recur(node.right)
        # In
        # self.print_tree_recur(node.left)
        # print(node.data)
        # self.print_tree_recur(node.right)

        # Post
        # self.print_tree_recur(node.left)
        # self.print_tree_recur(node.right)
        # print(node.data)


tree = BinaryTree()
tree.populate_tree()
tree.print_tree()

