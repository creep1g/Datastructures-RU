class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.center = None

# Implement helper classes here

class LRCMap:
    def __init__(self, build = False):
        self.root = None

        if build:
            self.root = self._build(8)
        else:
            self.root = Node()

    def _build(self, levels):
        if levels < 0:
            return None
        node = Node()
        node.right = self._build(levels - 1)
        node.center = self._build(levels - 1)
        node.left = self._build(levels - 1)
        return node

    def put_data(self, key, data):
        self._put_recur(self.root, key, data)

    def _put_recur(self, node, key, data):
        if node is None:
            node = Node()
        if key == "":
            node.data = data
        elif key[0] == 'l':
            node.left = self._put_recur(node.left, key[1:], data)
        elif key[0] == 'c':
            node.center = self._put_recur(node.center, key[1:], data)
        elif key[0] == 'r':
            node.right = self._put_recur(node.right, key[1:], data)
        return node

    def get_data(self, key): # returns data for that key or None if non-existant
        node = self._get_recur(self.root, key)
        if node is not None:
            return node.data
        else:
            return None

    def _get_recur(self, node, key):
        if node is None:
            return None

        if key == '':
            return node

        elif key[0] == 'l':
            node = self._get_recur(node.left, key[1:])
        elif key[0] == 'c':
            node = self._get_recur(node.center, key[1:])
        elif key[0] == 'r':
            node = self._get_recur(node.right, key[1:])
        
        return node

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    tm = LRCMap()
    tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")
    tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")
    print(tm.get_data("lrl"))
    print(tm.get_data("lrcclc"))
    print(tm.get_data("lc"))

    tm = LRCMap(True)
    tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")
    tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")
    print(tm.get_data("lrlrcclc"))
    print(tm.get_data("lrlclc"))
    print(tm.get_data("lrlrccr"))
