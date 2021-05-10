## SCRABBLE! 

You can run this game by typing ``python game.py`` <br>

Firstly you are prompted with a greeter that asks you if you want to play or read the rules of scrabble <br>
```
Welcome to scrabble!
Enter "r" to view the rules of scrabble
"p" to play or you can enter "q" to quit: p
```
Next you are asked how many will be playing
```
How many will be playng the game?(min 2 max 4): 2
Please enter player 1 name: aoeu
Please enter player 2 name: aoeu
```

After that each player gets assigned a tile that is drawn randomly from the bag.<br>
The player with the tile closest to A gets to go first.

```
Each player will draw a tile, whoever draws the tile closest to 'A'goes first!
aoeu drew D. aoeu drew U. aoeu Goes first
```

Now the **GAME** starts!

```
   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
  ----------------------------------------------
A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
D |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
E |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
F |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
G |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
H |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
I |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
J |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
K |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
M |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
O |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
```

This is the board, I did not have time to add modifier squares, on this we will place our tiles

Since this is the first round the position is predefined, that is the first letter will start on the center square.

Each turn the information for the player who's turn it is.
```
Turn: 
Name: aoeu
Letters: V J E N A R F 
Score: 0
```

Every round the player has a choice of three, play word, swap tiles, or forfeit their turn

```
        Select 1 to play a word
        2 to swap any tiles
        or 3 to forfeit turn
```

For the first turn the player who's turn it is only has to choose which direction the word will go

When player decides to play a word they are firstly asked to select a starting column then they select the row after that they select a direction.

```
1
What column? (1..15): 9
What row?(A..O): G
What Direction?(D: Down, A: Accross): D  
Enter word: FRE
Score: 7
   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
  ----------------------------------------------
A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
D |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
E |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
F |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
G |  |  |  |  |  |  |  |  |F |  |  |  |  |  |  |
  ----------------------------------------------
H |  |  |  |  |  |  |  |L |I |E |  |  |  |  |  |
  ----------------------------------------------
I |  |  |  |  |  |  |  |  |R |  |  |  |  |  |  |
  ----------------------------------------------
J |  |  |  |  |  |  |  |  |E |  |  |  |  |  |  |
  ----------------------------------------------
K |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
M |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
O |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15

```

It is important when a word starts with a tile from a word already on the board
that that the starting row, if word is going down or the starting column if its going across is the square that the letter that starts the word is placed in.

```
What column? (1..15): 8
What row?(A..O): J
What Direction?(D: Down, A: Accross): D
Enter word: IG
Score: 18
   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
  ----------------------------------------------
A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
D |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
E |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
F |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
G |  |  |  |  |  |  |  |  |F |  |  |  |  |  |  |
  ----------------------------------------------
H |  |  |  |  |  |  |  |L |I |E |  |  |  |  |  |
  ----------------------------------------------
I |  |  |  |  |  |  |  |  |R |  |S |  |  |  |  |
  ----------------------------------------------
J |  |  |  |  |  |  |  |B |E |A |T |  |  |  |  |
  ----------------------------------------------
K |  |  |  |  |  |  |  |I |  |  |I |  |  |  |  |
  ----------------------------------------------
L |  |  |  |  |  |  |  |G |  |  |N |  |H |  |  |
  ----------------------------------------------
M |  |  |  |  |  |  |  |  |  |  |G |O |A |T |  |
  ----------------------------------------------
N |  |  |  |  |  |  |  |  |  |  |  |  |T |  |  |
  ----------------------------------------------
O |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  ----------------------------------------------
   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
```


This project is not fully functional do to personal time constraints, there are some bugs regarding adding a word as well as some functionality (modifier tiles) are missing.


