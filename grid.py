import os

class Grid():
    # Create the grid
    def __init__(self, y, x):
        self.grid = [[False]*y for i in range(x)]
        self.new_grid = [[False]*y for i in range(x)]

    # Get the grid
    def get_grid(self):
        return self.grid

    # Update the grid
    def set_grid(self, new_grid):
        self.grid = new_grid
        self.new_grid = [[False]*(len(self.new_grid)) \
                for i in range((len(self.new_grid)))]

    # Get a grid bit
    def get_bit(self, y, x):
        return self.grid[y][x]

    # Set a grid bit
    def set_bit(self, y, x, value):
        self.grid[y][x] = value

    # Print the grid
    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        for i in range(len(self.grid) * 2 + 3):
            print("=", end="")
        print("")
        for i in range(len(self.grid)):
            print("|", end=" ")
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == True:
                    print("o", end=" ")
                else:
                    print("-", end=" ")
            print("|")
        for i in range(len(self.grid) * 2 + 3):
            print("=", end="")
        print("")

    # Find number of adjacent bits that are 'true'
    def get_adjacent(self, y, x):
        adjacent = 0
        corner1 = 0     # Smallest y and x corner
        corner2 = 0     # Smaller y, larger x corner
        corner3 = 0     # Larger y, smaller x corner
        corner4 = 0     # Largest y and x corner
        if y > 0:
            adjacent += self.grid[y - 1][x]
            corner1 += 1
            corner2 += 1
        if y < len(self.grid):
            adjacent += self.grid[y + 1][x]
            corner3 += 1
            corner4 += 1
        if x > 0:
            adjacent += self.grid[y][x - 1]
            corner1 += 1
            corner3 += 1
        if x < len(self.grid[0]):
            adjacent += self.grid[y][x + 1]
            corner2 += 1
            corner4 += 1
        if corner1 == 2:
            adjacent += self.grid[y - 1][x - 1]
        if corner2 == 2:
            adjacent += self.grid[y - 1][x + 1]
        if corner3 == 2:
            adjacent += self.grid[y + 1][x - 1]
        if corner4 == 2:
            adjacent += self.grid[y + 1][x + 1]
        return adjacent

    # Update a bit
    def update_bit(self, y, x):
        adj = self.get_adjacent(y, x)
        if self.grid[y][x] == True:
            if adj <= 1:
                self.new_grid[y][x] = False
            elif adj >= 4:
                self.new_grid[y][x] = False
            else:
                self.new_grid[y][x] = True
        else:
            if adj == 3:
                self.new_grid[y][x] = True
            else:
                self.new_grid[y][x] = False

    # Update the grid
    def update_grid(self):
        self.new_grid = [[False]*(len(self.new_grid)) \
                for i in range((len(self.new_grid)))]
        for i in range(len(self.grid) - 1):
            for j in range(len(self.grid[i]) - 1):
                self.update_bit(i, j)
        self.grid = self.new_grid

"""
 1  2  3
 4  *  5
 6  7  8

i.e.,

[0][0]   [0][1]   [0][2]
[1][0]   [1][1]   [1][2]
[2][0]   [2][1]   [2][2]
"""
