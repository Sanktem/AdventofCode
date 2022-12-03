#Advent of Code Day 3
#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52.

with open ('/home/sanktem/Desktop/Scripting/AdventofCode/Day3/data.txt', 'r') as f:
    line = f.readlines()
    for pack in line:
        print(pack.strip())