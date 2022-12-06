#Advent of code Day 5
#Find the crates on the top of each stack

#stacks = [['R','S','L','F','Q'], ['N','Z','Q','G','P','T'],  ['S','M','Q','B'], ['T','G','Z','J','H','C','B','Q'], ['P','H','M','B','N','F','S'], ['P','C','Q','N','S','L','V','G'], ['W','C','F'], ['Q','H','G','Z','W','V','P','M'], ['G','Z','D','L','C','N','R']]

from array import *

def  PartOne ():
    stacks = [['R','S','L','F','Q'], ['N','Z','Q','G','P','T'],  ['S','M','Q','B'], ['T','G','Z','J','H','C','B','Q'], ['P','H','M','B','N','F','S'], ['P','C','Q','N','S','L','V','G'], ['W','C','F'], ['Q','H','G','Z','W','V','P','M'], ['G','Z','D','L','C','N','R']]
    with open ('A:\Documents\GitHub\AdventofCode\AdventofCode\Day5\data.txt', 'r') as f:
        line = f.readlines()
        for box in line:
            i = 0
            move = [*map(int, box.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(','))]
            move[1] -= 1
            move[2] -= 1
            while i < move[0]:
                last = stacks[move[1]][-1]
                stacks[move[1]].pop()
                stacks[move[2]].append(last)
                i += 1
    final = [stacks[0][-1], stacks[1][-1], stacks[2][-1], stacks[3][-1], stacks[4][-1], stacks[5][-1], stacks[6][-1], stacks[7][-1], stacks[8][-1]]
    return ''.join(final)

def  PartTwo ():
    stacks = [['R','S','L','F','Q'], ['N','Z','Q','G','P','T'],  ['S','M','Q','B'], ['T','G','Z','J','H','C','B','Q'], ['P','H','M','B','N','F','S'], ['P','C','Q','N','S','L','V','G'], ['W','C','F'], ['Q','H','G','Z','W','V','P','M'], ['G','Z','D','L','C','N','R']]
    with open ('A:\Documents\GitHub\AdventofCode\AdventofCode\Day5\data.txt', 'r') as f:
        line = f.readlines()
        for box in line:
            i = 0
            j = 0
            move = [*map(int, box.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(','))]
            move[1] -= 1
            move[2] -= 1
            moving = []
            print(move[1], move[0])
            last = stacks[move[1]][-move[0]]
            print(last)
            ###Need to find a way to deal with this index error that is showing up
            # while i < move[0]:
            #     last = stacks[move[1]][move[0] * -1]
            #     moving.append(last)
            #     del last
            #     move[0] -= 1
            #     i += 1
            # for item in moving:
            #     stacks[move[2]].append(item)

    final = [stacks[0][-1], stacks[1][-1], stacks[2][-1], stacks[3][-1], stacks[4][-1], stacks[5][-1], stacks[6][-1], stacks[7][-1], stacks[8][-1]]
    return ''.join(final)

def test():
    q = [1, 2, 3]
    g = [4, 5, 6]
    for item in g:
        q.append(item)

    return q[-2]

print('PartOne top of stacks', PartOne())
print('PartTwo top of stacks', PartTwo())

#print(test())
