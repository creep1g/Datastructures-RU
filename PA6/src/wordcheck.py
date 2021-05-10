class WordChecker:

    def __init__(self, board):
        self.board = board
        self.dictionary = self.open_dict()

    def open_dict(self):
        words = []
        with open("src/words.txt", "r") as dictionary:
            for line in dictionary.readlines()[2:]:
                words.append(line.split("\t")[0])
    
        return words

    def check_word(self, word):
        '''Checks if word is in dictionary, returns True if exists, else
        False'''
        return word.upper() in self.dictionary


if __name__ == "__main__":
    chu = WordChecker("A")
    print(chu.check_word("aoeu"))
    print(chu.check_word("Average"))


