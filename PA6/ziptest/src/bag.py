from src.letters import *
from src.tiles import Tile
import random

class TileBag:
    '''Class representing a bag of tiles'''

    def __init__(self):
        '''Initialize bag as an empty list and add each tile to the bag'''
        self.tileBag = []
        self.__generate_bag()

    def isEmpty(self):
        if self.tileBag == []:
            return True
        else:
            return False

    def put_in_bag(self, char, amount=1):
        '''Adds tiles to the bag'''
        if amount < 1:
            return
        else:
            self.tileBag.append(char)
            self.put_in_bag(char, amount-1)
        
        random.shuffle(self.tileBag) #  SHAKE THE BAG!!!
    
    def __generate_bag(self):
        '''Generates starting bag''' 
        for key in CHAR_VALS:
            self.put_in_bag(Tile(key, CHAR_VALS[key]), CHAR_COUNT[key])

    def draw(self):
        return self.tileBag.pop(random.randint(0, len(self.tileBag)-1))

    def __len__(self):
        '''Returns tile count in bag'''
        return len(self.tileBag)

    def __str__(self):
        '''Returns stringified version of the bag'''
        ret_str = ""
        for tile in self.tileBag:
            ret_str += "{} ".format(str(tile))
        return ret_str


if __name__ == "__main__":
    bag = TileBag()

    print(len(bag))
    print(bag.draw())
    print(len(bag))
    print(bag)
