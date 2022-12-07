#Advent Of Code Day 7

from array import *
import os

def PartOne():
    tab = '    '
    with open ('data.txt', 'r') as data, open ('output.txt', 'a') as output:
        line = data.readlines()
        i = 0
        for command in line:
            cmd = command.split(' ')
            if (cmd[0] == '$') and (cmd[1] == 'cd'):
                 print(y)



            


def test(): 
    test_list = [[[1,2,3],[1,2,'this one'],[1,2,3]], [1,2,3]]
    print(test_list[0][1][2])

os.remove('output.txt')
PartOne()
#test()