import webbrowser
import time
from src.letters import *
from src.board import Board
from src.player import Player
from src.bag import TileBag
from src.wordcheck import WordChecker


def intro():
    print('Welcome to scrabble!')
    init = ''
    while init.lower() != 'q':
        print('Enter "r" to view the rules of scrabble\n"p" to play or you can enter "q" to quit: ', end='')
        init = input() 
        if init.lower() == 'r':
            '''Opens up the official rulebook of scrabble'''
            url = 'http://www.scrabblepages.com/scrabble/rules/'
            print("Let me just open {} for you quickly!".format(url))
            time.sleep(1)
            webbrowser.open(url)
            print("There you go!")
            print('\n')

        elif init.lower() == 'p':
            return get_players()

        elif init.lower == 'q':
            print("Thank you, come again!")
            return None, None

        else:
            print("{} is not a valid input. Please try again".format(init))


def get_players():
    '''Asks user for information about amount of players and generates a list
    of player instances'''

    amount = ''
    tileBag = TileBag()
    while amount.lower() != 'q':
        amount = input("How many will be playng the game?(min 2 max 4): ")
        if amount.isdigit() and 2 <= int(amount) <= 4:
            player_list = []
            for i in range(int(amount)):
                player = input('Please enter player {} name: '.format(str(i+1)))
                player_list.append(Player(player, tileBag))
            break
        else:
            print("{} is not a valid choice, please make sure you input a\
                    number between 1 and 4.".format(amount))
            print("HINT: You can also enter 'q' to quit")
            print('\n')

    if amount.lower() != 'q':
        return (player_list, tileBag)
    else:
        return None, None

def start_game(player_list, tileBag):
    print("Each player will draw a tile, whoever draws the tile closest to 'A'\
goes first!")
    compare_dict = dict()
    count = 0
    info_string = ""

    for player in player_list:
        player.draw_tile(1)
        compare_dict[count] = ord(player.get_letters_str()[0])
        info_string += "{} drew {}. ".format(player_list[count].get_name(),
                                     player_list[count].get_letters_str()[0])
        count += 1

    first = ""
    for key in compare_dict:
        if first == "":
            first = key
        if compare_dict[key] < compare_dict[first]:
            first = key

    info_string += "{} Goes first".format(player_list[int(first)].get_name())
    print(info_string) 
    print()
    print()
    time.sleep(1)
    for player in player_list:
        player.return_tile(1)
        player.draw_tile(7)
    
    board = Board()
    gameloop(player_list, board, tileBag, first)

def round(player, tileBag, board, wordChecker):
    '''Displays player information, allows player to select what he wants to do
    '''
    print("Turn: ")
    print(player)
    while True:
        print('''
        Select 1 to play a word
        2 to swap any tiles
        or 3 to forfeit turn
        ''')
        while True:
            choice = input()
            if choice.isdigit() and 0 < int(choice) < 4:
                choice = int(choice)
                break
        
        if board.isEmpty():
            col = 7
            row = "H"

        if choice == 1:
            while True:
                if not board.isEmpty():
                    while True:
                        col = input("What column? (1..15): ")
                        if col.isdigit():
                            col = int(col)-1
                            break
                    while True:
                        row = input("What row?(A..O): ").upper()
                        if row.upper() in board.get_rows():
                            break
                    
                while True:
                    dire = input("What Direction?(D: Down, A: Accross): ")

                    if dire.upper() == "A":
                        dire = 1
                        break

                    elif dire.upper() == "D":
                        dire = 0
                        break

                word = input("Enter word: ").upper()
                if player.check_if_valid(word):  # Makes sure you have tiles
                    score = board.check_combined(row, col, word.upper(), dire)
                    if score > 0:
                        if board.isEmpty():
                            score *= 2  # First word gets *2 modifier
                        status = board.add_to_board(row, col, word.upper(), dire)
                        if status == 200:
                            player.pop_letters(word)

                            if player.how_many() == 7:
                                score += 50  # +50 if all tiles are used

                            player.add_to_score(score)
                            player.draw_tile(player.how_many())
                            print("Score: " + str(player.get_score()))
                            time.sleep(0.5)
                            return

                    elif score == -1:
                        print("Word must touch atleast one tile on the board!")

                    else:
                        print("Word is not allowed, you have forfeited your turn.")
                        time.sleep(1)
                        return
                else:
                    print("You do not have the tiles to play this word!")
        
        elif choice == 2:
            player.return_tile(7)
            player.draw_tile(7)
            print("New hand: {}".format(player.get_letters_str()))
            break

        elif choice == 3:
            return True

        else:
            print("{} is not a valid choice.".format(choice))


def is_winner(players, tileBag, skip_count):
    '''If bag is empty and player has used all his tiles he'''
    player = None
    for dude in players:
        if len(dude.get_letters()) == 0:
            player = dude

    if player is None:
        player = players[0]

    if ((tileBag.isEmpty() and len(player.get_letters()) == 0) or
                                    skip_count==2*len(players)):
        return True
    return False


def declare_winner(player, players):
    '''Declares winner, '''
    if len(player.get_letters()) > 0:
        for person in player_list:
            for tile in person.get_letters():
                person.add_to_score(CHAR_VALS[tile.get_char()])
    highest = 0
    winner = None
    for person in players:
        if person.get_score() > highest:
            highest = person.get_score()
            winner = person

    print()
    print("############WINNER################")
    print(winner)


def gameloop(players, board, tileBag, first):
    '''Loops until game is over'''
    round_counter = first
    wordChecker = WordChecker(board)
    skip_count = 0
    while is_winner(players, tileBag, skip_count) is not True:
        print(board)
        skipped = round(players[round_counter % len(players)], tileBag, board,
                                                                  wordChecker)
        if skipped:
            skip_count += 1
        else:
            skip_count = 0

        if is_winner(players, tileBag, skip_count):
            declare_winner(players[round_counter % len(players)], player_list)
            break

        round_counter += 1


if __name__ == '__main__':
    player_list, tileBag = intro()
    if player_list and tileBag:
        start_game(player_list, tileBag)
    else: 
        print("Quitting!")
