from src.tiles import Tile
from src.bag import TileBag
from src.letters import *


class Hand:

    def __init__(self, tileBag):
        self.arr = []
        self.tileBag = tileBag

    def draw(self, amount=1):
        '''Pulls *amount* many tiles from tile bag'''
        if amount < 1:
            return
        else:
            self.arr.append(self.tileBag.draw())
            self.draw(amount-1)

    def is_in(self, char):
        '''Returns true if charachter is in array, else return false'''
        for tile in self.arr:
            if char == tile.get_char():
                return True

        return False

    def discard_tile(self, char):
        for tile in self.arr:
            if tile.char == char.upper():
                self.arr.remove(tile)
    
    def return_tile(self, amount=1):
        if amount < 1:
            return
        else:
            char = self.arr.pop(0).get_char()
            self.tileBag.put_in_bag(Tile(char, CHAR_VALS[char]))
            self.return_tile(amount - 1)

    def play_tile(self, tile):
        '''Pull tile off players hand'''
        self.arr.remove(tile)

    def get_hand(self):
        return self.arr

    def __str__(self):
        '''Stringfy palyer hand'''
        ret_str = ""
        for tile in self.arr:
            ret_str += tile.get_char() + " "
        return ret_str

    def __len__(self):
        return len(self.arr)

if __name__ == "__main__":
    bag = TileBag()
    hand = Hand(bag)
    print(hand)
    hand.play_tile(hand.arr[3])
    print(hand)
    print(len(hand))
