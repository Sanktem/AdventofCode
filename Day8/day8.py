#Advent of code day 8

from array import *

with open ('./data.txt', 'r') as f:
    line = f.read().splitlines()
    grid = []
    for row_one in line:
        tree = row.split()
        grid.append(list(tree[0]))


print(len(grid[0]))
