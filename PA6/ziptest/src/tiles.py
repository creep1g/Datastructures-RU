class Tile:
    '''Class representing each tile in scrabble'''
    def __init__(self, char, value):
        self.char = char
        self.value = value

    def get_char(self):
        return self.char

    def get_val(self):
        return self.value

    def __str__(self):
        return "{}:{}".format(self.char, self.value)


if __name__ == "__main__":
    tile = Tile("A", 22)
    print(tile.get_val())
    print(tile.get_char())
