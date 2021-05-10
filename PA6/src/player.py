from src.playerHand import Hand

class Player:

    def __init__(self, name, tileBag):
        '''Initialize player with names, empty letter board, and score'''
        self.name = name
        self.score = 0
        self.hand = Hand(tileBag)

    def add_to_score(self, int_val):
        '''Adds new score to player'''
        self.score += int_val

    def check_if_valid(self, string):
        '''Checks if user has the letters to play a given word'''
        for char in string:
            boolean = self.hand.is_in(char)
            if not boolean:
                return False

        return True

    def pop_letters(self, string):
        '''Removes letters from array'''
        for i in string:
            self.hand.discard_tile(i)

    def get_letters(self):
        '''Returns array of letters'''
        return self.hand.get_hand()

    def draw_tile(self, amount=1):
        self.hand.draw(amount)

    def return_tile(self, amount=1):
        self.hand.return_tile(amount)

    def how_many(self):
        '''Returns amount of tiles to draw'''
        return 7 - len(self.hand)

    def get_letters_str(self):
        '''Returns stringified version of letters'''
        return str(self.hand)

    def get_score(self):
        '''Returns players score'''
        return self.score

    def get_name(self):
        return self.name

    def __str__(self):
        letters = self.get_letters_str()
        return ("Name: " + self.name + "\n" +
                "Letters: " + str(self.hand) + "\n" +
                "Score: " + str(self.score))


if __name__ == '__main__':
    player = Player(21, "Gustaf")
    player.add_letters(arr=["a", "b", "c", "z"])
    player.add_to_score(2)
    player.get_letters()
    print(player.check_if_valid("a"))
    print(player.get_letters())
    print(player.get_letters_str())
    print(player.how_many())
    print(player)
