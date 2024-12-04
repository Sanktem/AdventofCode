#Advent of code Day 9
#Find the positions that the tail has been in a grid

def PartOne():
    with open ('data.txt', 'r') as f:
        line = f.readlines()
        gridpos = [0,0]
        newpos = 0
        for pos in line:
            cmd = pos.strip().split(' ')
            print(cmd)
            if cmd[0] == 'D':
                for v in range(1, cmd[1]):
                    newpos += 1
                gridpos[1] -= cmd[1]
PartOne()