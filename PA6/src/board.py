from src.wordcheck import WordChecker
from src.letters import *

class WordNotAllowed(Exception):
    pass


class Board:

    def __init__(self):
        self.board = dict()
        self.gen_board()
        self.wordChecker = WordChecker(self)
        self.stack = []  # Used to roll back if word does not fit
        self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                     "L", "M", "N", "O"]

        self.empty = True

    def get_rows(self):
        return self.rows
    
    def isEmpty(self):
        return self.empty
    
    def gen_board(self):
        '''Generates 15x15 b ard rows = A-O, cols = 1-15'''
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                     "L", "M", "N", "O"]
        for row in rows:
            self.board[row] = [" "] * 15

    def check_combined(self, row, col, word, direction):
    
        '''Checks if word is combined with another word'''
        score = 0
        combined_word = ""
        exclude = (None, None)
        rowptr = row
        colptr = col
        # check right / down
        for char in word.upper():
            if (self.board[rowptr][colptr] != " "):
                combined_word += self.board[rowptr][colptr]
                exclude = (rowptr, colptr)
            combined_word += char
                        
            if direction == 0:
                rowptr = chr(ord(rowptr) + 1)
            else:
                colptr += 1
        if direction == 0:
            rowptr = chr(ord(rowptr) + 1)
            if self.board[rowptr][col] != " ":
                combined_word += self.board[rowptr][colptr]
                print(combined_word)
            
        word_list = self.check_around(row, col, combined_word, direction,
                                          exclude)
        print(word_list)
        for i in word_list:
            if self.wordChecker.check_word(i):
                score += self.calculate_score(i)
#            else:
 #               return 0

        return score

    def check_around(self, row, col, word, direction, exclude):
        '''Checks for surrounding words and returns a list of words'''
        words = []
        ex_row, ex_col = exclude
        char_list = [char for char in word]
        if direction == 0:
            # Check top of word
            rowptr = chr(ord(row) - 1)
            while ord(rowptr) > ord("A")-1:
                if self.board[rowptr][col] != " ":
                    char_list.insert(0, self.board[rowptr][col])
                    rowptr = chr(ord(rowptr) - 1)
                else:
                    break


            rowptr = chr(len(char_list) + ord(row))
            # Check bottom of word
            while ord(rowptr) < ord("O")+1:
                if self.board[rowptr][col] != " ":

                    if col != ex_col and rowptr != ex_row:
                        char_list.append(self.board[rowptr][col])
                    rowptr = chr(ord(rowptr) + 1)
                else:
                    break
            words.append("".join(char_list))

            rowptr = row
            colptr = col
            for char in word:
                comb_word = ""
                if rowptr > "O":
                    break
                if col != ex_col and rowptr != ex_row:
                    if col-1 >= 0 and self.board[rowptr][colptr-1] != " ":
                        left = self.get_word(rowptr, col-1, "left")
                        comb_word += left
                    comb_word += char

                    if col+1 <= 14 and self.board[rowptr][col+1] != " ":
                        right = self.get_word(rowptr, col+1, "right")
                        comb_word += right

                    if len(comb_word) > 1:
                        words.append(comb_word)
                rowptr = chr(ord(rowptr) + 1)

        elif direction == 1:
            # check right of
            colptr = col - 1
            while colptr >= 0:
                if self.board[row][colptr] != " ":
                    if colptr != ex_col and row != ex_row:
                        char_list.insert(0, self.board[row][colptr])
                    colptr -= 1
                else: 
                    break
            colptr = col+len(word)

            while colptr <= 14:
                if self.board[row][colptr] != " ":
                    if colptr != ex_col and row != ex_row:
                        char_list.append(self.board[row][colptr])
                    colptr += 1
                else:
                    break

            words.append("".join(char_list))
            colptr = col
            up = chr(ord(row) - 1)
            down = chr(ord(row) + 1)
            for char in word:
                comb_word = ""
                if colptr > 14:
                    break
                if colptr != ex_col and row != ex_row:
                    if up >= "A" and self.board[up][colptr] != " ":
                        top = self.get_word(up, colptr, "up")
                        comb_word += top

                    comb_word += char

                    if down <= "O" and self.board[down][colptr] != " ":
                        bottom = self.get_word(down, colptr, "down")
                        comb_word += bottom
                if len(comb_word) > 1:
                    words.append(comb_word)

        return words

    def calculate_score(self, words):
        score = 0
        for word in words:
            for char in word:
                score += CHAR_VALS[char]
        return score

    def get_word(self, row, col, direction):
        '''Gets word?'''
        dirs = ["up", "down", "left", "right"]
        word = ""
        while self.board[row][col] != " ":
            word += self.board[row][col]

            if direction == dirs[0]:
                row = chr(ord(row) - 1)

            if direction == dirs[1]:
                row = chr(ord(row) + 1)

            if row < "A" or row > "O":
                break

            if direction == dirs[2]:
                col = col-1

            if direction == dirs[3]:
                col = col+1

            if col < 0 or col > 14:
                break

        return word

    def add_to_board(self, row, col, string, direction):
        '''Iterates over string adding it to its correct row:col position
        according to given direction, if that word is not in our dictonary
        error code is returned, if the word does not fit on the board return
        error code'''
        # Check if word fits
        # Check if adjacent word
        # If it does not fit ask send Errcode
        # If it does fit update board
        try:
            for let in string.upper():
                if self.board[row][col] != " ":
                    while True:
                        if self.board[row][col] == " ":
                            self.board[row][col] = let
                            break
                        else:
                            if direction == 0:
                                row = chr(ord(row) + 1)
                            else:
                                col += 1
                self.board[row][col] = let
                self.stack.insert(0, (let, col, row))
                
                if direction == 0:
                    row = chr(ord(row) + 1)
                else:
                    col += 1

            self.stack = []
            self.empty = False
            return 200

        except KeyError:
            self.__rollback()
            self.stack = []
            return 221  # Code 221 == word does not fit

    def __rollback(self):
        '''Removes added letters'''
        for i in self.stack:
            let, col, row = i
            self.board[row][col] = " "

    def __str__(self):
        number_row = ('   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15\n')
        ret_str = number_row
        line = "-" * 46
        for key, value in self.board.items():
            ret_str += "  " + line + "\n"
            ret_str += "{} |".format(key)
            for square in value:
                ret_str += square + " |"
            ret_str += "\n"
        ret_str += '  ' + line + "\n"
        ret_str += number_row

        return ret_str


if __name__ == "__main__":
    board = Board()
    print(board)
    board.add_to_board("A", 2-1, "Decan", 1)
    board.add_to_board("F", 1, "Sweep", 0)
    print(board)
    print(board.add_to_board("B", 1, "metal", 0))
    print(board)
    print(board.add_to_board("B", 1, "meoauugcrl", 0))
