#advent of code day 4 these elf's are a fucking desastier
#find the data pairs that contain eachother

def Partone():
    partone_score = 0
    with open ('A:\Documents\GitHub\AdventofCode\AdventofCode\Day4\datafull.txt', 'r') as f:
        line = f.readlines()
        for space in line:
            elf = [*map (int, space.replace('-', ',').split(','))]
            if  (elf[0] >= elf[2]) and (elf[1] <= elf[3]):
                partone_score += 1
            elif (elf[0] <= elf[2]) and (elf[1] >= elf[3]):
                partone_score += 1
            else:
                pass
    return partone_score

def Parttwo():
    parttwo_score = 0
    with open ('A:\Documents\GitHub\AdventofCode\AdventofCode\Day4\datafull.txt', 'r') as f:
        line = f.readlines()
        for space in line:
            elf = [*map(int, space.replace('-', ',').split(','))]
            if  (elf[0] <= elf[2] <= elf[1]):
                parttwo_score += 1
            elif (elf[2] <= elf[0] <= elf[3]):
                parttwo_score += 1
            else:
                pass
    return parttwo_score
        

print('PartOne Score: ', Partone())
print('PartTwo Score: ', Parttwo())