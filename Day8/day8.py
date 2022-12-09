#Advent of code day 8

from array import *

def PartOne():
    with open ('./data.txt', 'r') as f:
        line = f.read().splitlines()
        grid = []
        score = 0
        for row_one in line:
            tree = row_one.split()
            grid.append([*map (int, list(tree[0]))])
        
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                tree = grid[i][j]
                if all(x < tree for x in grid[i][0:j]) or \
                    all(x < tree for x in grid[i][j+1:]) or \
                    all(x < tree for x in grid[j][0:i]) or \
                    all(x < tree for x in grid[j][i+1:]):
                    score += 1
    
    return score - 20

def PartTwo():
    with open ('./data.txt', 'r') as f:
        line = f.read().splitlines()
        grid = []
        score = 0
        for row_one in line:
            tree = row_one.split()
            grid.append([*map (int, list(tree[0]))])
        
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                tree = grid[i][j]
                if all(x < tree for x in grid[i][0:j]) or \
                    all(x < tree for x in grid[i][j+1:]) or \
                    all(x < tree for x in grid[j][0:i]) or \
                    all(x < tree for x in grid[j][i+1:]):
                    score += 1
    
    return score - 20

print('Part One is: ', PartOne())
