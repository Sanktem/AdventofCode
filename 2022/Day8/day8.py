#Advent of code day 8

from array import *

def PartOne():
    data = open('data.txt').readlines()

    grid = [[int(x) for x in row.strip()] for row in data]
    grid2 = list(zip(*grid))
    
    score = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            tree = grid[i][j]
            if all(x < tree for x in grid[i][0:j]) or \
                all(x < tree for x in grid[i][j+1:]) or \
                all(x < tree for x in grid2[j][0:i]) or \
                all(x < tree for x in grid2[j][i+1:]):
                score += 1
    
    return score

def view_length(tree, view):
    view_length = 0
    for v in view:
        view_length += 1
        if v >= tree:
            break
    return view_length

def PartTwo():
    data = open('data.txt').readlines()

    grid = [[int(x) for x in row.strip()] for row in data]
    grid2 = list(zip(*grid))
    
    s = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            tree = grid[i][j]
            s1 = view_length(tree, grid[i][0:j][::-1])
            s2 = view_length(tree, grid[i][j+1:])
            s3 = view_length(tree, grid2[j][0:i][::-1])
            s4 = view_length(tree, grid2[j][i+1:])
            score = s1 * s2 * s3 * s4
            if score > s:
                 s = score
    
    return s

print('Part One is: ', PartOne())
print('Part two is: ', PartTwo())