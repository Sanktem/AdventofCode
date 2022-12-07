#Advent of code day 6

from collections import Counter

def PartOne():
    with open ('data.txt', 'r') as f:
        for line in f:
            data = line.strip()
    
    for i in range(3, len(data)-3):
        marker = data[i-4:i]
        freq = Counter(marker)
        if len(freq) == 4:
            return i
            break

def PartTwo():
    with open ('data.txt', 'r') as f:
        for line in f:
            data = line.strip()
    
    for i in range(13, len(data)-13):
        marker = data[i-14:i]
        freq = Counter(marker)
        if len(freq) == 14:
            return i
            break



print('Part One Marker is: ', PartOne())
print('Part Two Message is: ', PartTwo())