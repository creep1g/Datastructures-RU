class Tree_Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def populate_tree(self):
        self.root = self.populate_tree_recur()

    def populate_tree_recur(self, parent_name="", level=0):
        tree = None
        data = ""
        if parent_name == "" and level == 0:
            data = input("Enter name of root: ")

        if data != "":
            tree = Tree_Node(data)
        else:
            return 
        while True:
            if data != "":
                tree.children.append(self.populate_tree_recur(data, level+1))
            else:
                data = input("Enter name of node child of " + parent_name)

                if data == "":
                    break
        return tree

    def print_tree(self):
        self.print_tree_recur(self.root)

    def print_tree_recur(self, node):
        if node == None:
            return

        print(node.data)
        for node in node.children:
            self.print_tree_recur(node)


tree = Tree()
tree.populate_tree()
tree.print_tree()

