#!/usr/bin/python3
"""
Conways Game of Life
by Callum France
"""
import time
from grid import Grid
import tumbler

# Create an empty board
board = Grid(11, 11)

# Turn the board into a tumbler
board.set_grid(tumbler.tumbler)

board.get_adjacent(0, 0)
print("Ran get adjacent")
board.update_bit(0, 0)

# Loop the Conway
for k in range(500):
    board.print_grid()
    board.update_grid()
    time.sleep(0.3)

# board.print_grid()
# board.update_grid()
# board.print_grid()
