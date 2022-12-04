#Advent of Code Day 3
#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52.


# stolen from u/nyuutsu - honelstly I'm really bad at programming, and I did not understand this one in the slightest

import string 

with open('A:\Documents\GitHub\AdventofCode\AdventofCode\Day3\datafull.txt', 'r') as file:
  sum = 0
  lines = file.readlines()
  for i in range(0, len(lines), 3):
    sum += int(string.ascii_letters.index(''.join(set(lines[i].strip()).intersection(lines[i+1].strip()).intersection(lines[i+2].strip())))) + 1
  print(f'Part 2: {sum}')