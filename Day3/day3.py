#Advent of Code Day 3
#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52.

with open ('/home/sanktem/Desktop/Scripting/AdventofCode/Day3/datafull.txt', 'r') as f:
    line = f.readlines()
    score = []
    anti_dupe = []
    for pack in line:
        half1 = pack[:len(pack)//2]
        half2 = pack[len(pack)//2:]
        print(half1, half2)
        for letter in half1:
            if letter in half2:
                anti_dupe.append(letter)
                if len(anti_dupe) != len(set(anti_dupe)):
                    #del anti_dupe[-1]
                    continue
                else:
                    print('Letter found: ', letter)
                    if letter.isupper() == True:
                        score.append(ord(letter) - 39)
                    else:
                        score.append(ord(letter) - 96)
        anti_dupe.clear()
    
    print(score)
    print('elements', len(score))
    print('Part One:', sum(score))

#below is stolen from KosmicAnomaly
# with open ('/hom8493e/sanktem/Desktop/Scripting/AdventofCode/Day3/datafull.txt', 'r') as f:
#     rucksacks = f.readlines()

# sum = 0

# priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for rucksack in rucksacks:
#     left = rucksack[: int(len(rucksack) / 2)]
#     right = rucksack[int(len(rucksack) / 2) :]

#     char = [c for c in left if c in right][0]

#     sum += 1 + priorities.rfind(char)

# print(sum)