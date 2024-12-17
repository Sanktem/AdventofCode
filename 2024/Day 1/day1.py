##AOC 2024 

##Day 1 Goal, finding the locations on the map by finding the lowest numbers, and subtracting them from eathother
##Data is in data.txt

from collections import Counter

def PartOne():
    Left_List = []
    Right_List = []
    Master_List = []
    Final_list = []
    count = 0
    with open ('data.txt', 'r') as f:
        for line in f:
            pairs = line.strip().split('   ')
            Left_List.append(int(pairs[0]))
            Right_List.append(int(pairs[1]))

        Left_List.sort()
        Right_List.sort()

        for cord in Right_List:
            Master_List.append(Left_List[count] - Right_List[count])
            count += 1

        for num in Master_List:
            if num < 0:
                Final_list.append(num * -1)
            else:
                Final_list.append(num)

    return sum(Final_list)

def PartTwo():
    Left_List = []
    Right_List = []
    master_list = []
    count = 0
    with open ('data.txt', 'r') as f:
        for line in f:
            pairs = line.strip().split('   ')
            Left_List.append(int(pairs[0]))
            Right_List.append(int(pairs[1]))
    
    for cord in Left_List:
        value = Counter(Right_List)
        master_list.append(Counter(Right_List)[Left_List[count]] * Left_List[count])
        count += 1

    return sum(master_list)
    
print('Part one is: ', PartOne())
print('Part two is: ', PartTwo())
