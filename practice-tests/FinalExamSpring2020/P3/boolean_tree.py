class BooleanNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class Tokenizer:

    def __init(self, statement):
        self.statement = statement
        self.pos = 0

    def get_next(self):
        i = self.pos
        while i < len(self.statement) and self.statement[i] != " ":
            i += 1
        ret = self.statement[self.position:i]
        self.pos = i + 1
        return ret_val

class BooleanTree:
    def __init__(self):
        self.root = None
        self.ops = ["OR", "AND"]
        self.vals = ["T", "F"]

    class Tokenizer:

        def __init__(self, statement):
            self.statement = statement
            self.pos = 0

        def get_next(self):
            ret = self.statement[self.pos]
            self.pos += 1
            return ret

    def build_tree(self, statement_string):
        statement_list = statement_string.replace("(", " ").replace(")", " ").replace(",", " ").split()
        tokenizer = self.Tokenizer(statement_list)
        self.root = self.build_tree_recursive(tokenizer)

    def build_tree_recursive(self, tokenizer):

        token = tokenizer.get_next()

        if token in self.ops:
            return BooleanNode(token, self.build_tree_recursive(tokenizer),
                    self.build_tree_recursive(tokenizer))
        elif token in self.vals:
            return BooleanNode(token, None, None)

        else:
            return BooleanNode(token, None, None)


    def get_root_value(self):
        value = self._traverse(self.root)
        return self.root.data == "T"

    def _traverse(self, node):
        if node is None:
            return
        self._traverse(node.left)
        self._traverse(node.right)
        if node.data in self.ops:
            left = node.left.data
            right = node.right.data

            if left in self.vals and right in self.vals:
                
                if node.data == "OR":
                    if left == "T" or right == "T":
                        node.data = "T"
                    else:
                        node.data = "F"

                if node.data == "AND":
                    if left == "T" and right == "T":
                        node.data = "T"
                    else:
                        node.data = "F"

    def __str__(self):
        return self.str_recur(self.root, "")

    def str_recur(self, root, ret_string):
        if root is None:
            return " "
        else:
            new_string = self.str_recur(root.left, ret_string)
            new_string += str(root.data)
            new_string += self.str_recur(root.right, ret_string)
            return new_string

# IMPLEMENT HERE

if __name__ == "__main__":

    print("\nSHOWING HOW TO LOSE THE DELIMITERS, IF WANTED")
    statement_string = "OR(AND(T,F),F)"
    print(statement_string)
    # YOU CAN DO THIS IN YOUR build_tree() OPERATION IF THE LIST FORMAT FEELS BETTER
    statement_list = statement_string.replace("(", " ").replace(")", " ").replace(",", " ").split()
    print(statement_list)


    print("\n\nTESTING BOOLEAN TREE\n")

    # THESE TESTS SHOULD WORK EXACTLY AS THEY ARE BUT FEEL FREE TO MAKE MORE EXTENSIVE TESTS AS WELL

    bt = BooleanTree()
    statement_string = "OR(AND(T,F),F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "OR(T,AND(T,F))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "OR(AND(T,T),F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(T,OR(F,F))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(OR(F,T),T)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(F,F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(OR(OR(F,F),T),OR(T,AND(T,F)))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
