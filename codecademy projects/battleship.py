# this program simulates a battleship game

from random import randint 

board = []

size = int(input("Please enter the number of rows and columns you would like: "))

for x in range(0, 5):
  board.append(["O"] * size)

def print_board(board_in):
  for row in board_in:
    print(" ".join(row))

print_board(board)

game_on = True

ship_row = randint(0, len(board)-1)
ship_col = randint(0, len(board)-1)
print(ship_row)
print(ship_col)

while(game_on==True):
    row_guess = int(input("Enter your row guess: "))
    col_guess = int(input("Enter your column guess: "))
    if(row_guess==ship_row and col_guess==ship_col):
        print("Hey! You sunk my battleship!")
        game_on=False
    else:
        print("Guess again!")
