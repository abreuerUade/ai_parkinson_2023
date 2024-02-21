import random

def factible(layout, pos):
    return not (layout[pos[0]-1][pos[1]-1] and layout[pos[0]][pos[1]-1] and layout[pos[0]-1][pos[1]] or layout[pos[0]][pos[1]-1] and layout[pos[0]+1][pos[1]-1] and layout[pos[0]+1][pos[1]] or     layout[pos[0]+1][pos[1]] and layout[pos[0]+1][pos[1]+1] and layout[pos[0]][pos[1]+1] or layout[pos[0]-1][pos[1]-1] and layout[pos[0]+1][pos[1]-1] and layout[pos[0]][pos[1]+1])

def genLayout(size):
    layout = [[True if x in [0, size-1] or y in [0, size-1] else False for x in range(size)] for y in range(size)]
    libres = []
    for y in range(1,size-1):
        for x in range(1,size-1):      
            if factible(layout, (x,y)) and not(x == size - 2 and y == 1):
                if not random.randint(0,2):
                    layout[x][y] = True
                else:
                    libres += [(x,y)]
    pacman = libres.pop(random.randint(0,len(libres)-1))
    goal = (1,size-2)
    arch = open(r"layouts\randomMaze.lay","w")
    for y in range(size):
        for x in range(size):
            if layout[x][y]: arch.write("%")
            elif pacman == (x,y): arch.write("P")
            elif goal == (x,y): arch.write(".")
            else: arch.write(" ")
        arch.write("\n")
    arch.close()

genLayout(40)