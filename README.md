# Conways_Game_of_Life
The 0 player game

Uses a 'grid' class and a class that holds a starting 'grid' (in this case the tumbler). Loads the game with the starting grid, and executes itself. The rules are simple:

- Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
