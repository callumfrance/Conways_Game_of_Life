tumbler = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], \
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], \
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], \
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0,], \
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,], \
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,], \
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,], \
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0,], \
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0,], \
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], \
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]]

quick = [ [0, 1, 0, 0, 0], \
         [1, 0, 0, 1, 0], \
         [0, 1, 1, 1, 0], \
         [0, 1, 0, 0, 1], \
         [0, 0, 0, 1, 0]]

explode = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

"""
print(tumbler)

os.system('cls' if os.name == 'nt' else 'clear')

print("=========================")
for i in range(len(tumbler)):
    print("|", end=" ")
    for j in range(len(tumbler[i])):
        if tumbler[i][j] == True:
            print("o", end=" ")
        else:
            print("-", end=" ")
    print("|")
print("=========================")
"""
