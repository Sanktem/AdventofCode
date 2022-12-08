#Advent Of Code Day 7

from collections import defaultdict
from math import inf
from os import path, sep

def PartOne():
    p1 = 0
    cwd = ''
    dir_sizes = defaultdict(int)
    with open('./data.txt', 'r') as f:
        for line in f:
            cmd = line.strip().split(' ')
            if cmd[0] == '$' and cmd[1] == 'cd':
                cwd = path.normpath(path.join(cwd, cmd[2]))
            
            if cmd[0].isnumeric():
                dirs = cwd.split(sep)
                for i in range(len(dirs)):
                    dir_path = path.normpath(path.join(*dirs[: i + 1]))
                    dir_sizes[dir_path] += int(cmd[0])
    
    sizes = dir_sizes.values()

    p1 = sum((v for v in sizes if v <= 1e5))

    return p1

def PartTwo():
    p2 = 0
    cwd = ''
    dir_sizes = defaultdict(int)
    with open('./data.txt', 'r') as f:
        for line in f:
            cmd = line.strip().split(' ')
            if cmd[0] == '$' and cmd[1] == 'cd':
                cwd = path.normpath(path.join(cwd, cmd[2]))
            
            if cmd[0].isnumeric():
                dirs = cwd.split(sep)
                for i in range(len(dirs)):
                    dir_path = path.normpath(path.join(*dirs[: i + 1]))
                    dir_sizes[dir_path] += int(cmd[0])
    
    avail_space = 7e7 - dir_sizes["."]
    sizes = dir_sizes.values()
    p2 = min((v for v in sizes if v + avail_space >= 3e7))
    
    return p2

print('Part one is: ', PartOne())
print('Part two is: ', PartTwo())