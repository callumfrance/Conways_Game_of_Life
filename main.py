#!/usr/bin/python3
"""
Conways Game of Life
by Callum France
"""
import time
from grid import Grid
import boardStarts

# Choose the conway board
print("Which board to use?")
choiceNum = int(input("> "))
# A "switch" statement...
if choiceNum == 0:
    board = Grid(11, 11)
    board.set_grid(boardStarts.tumbler)
elif choiceNum == 1:
    board = Grid(5, 5)
    board.set_grid(boardStarts.quick)
elif choiceNum == 2:
    board = Grid(13, 13)
    board.set_grid(boardStarts.explode)
else:
    print("else", choiceNum)
    board = Grid(11, 11)
    board.set_grid(boardStarts.tumbler)

# Loop the Conway
for k in range(500):
    board.print_grid()
    board.update_grid()
    time.sleep(0.3)
