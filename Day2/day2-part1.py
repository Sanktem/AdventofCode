#Advent of Code Day 2
#A, B, C is their choice, and X(1), Y(2), Z(3), is mine
#win(6), lose(0), draw(3)

with open ('/home/sanktem/Desktop/Scripting/AdventofCode/Day2/data.txt', 'r') as f:
    line = f.readlines()
    point_total = 0
    for match in line:
        their_hand = match[0].strip()
        my_hand = match[2].strip()

        if my_hand == 'X':
            point_total += 1
        elif my_hand == 'Y':
            point_total += 2
        elif my_hand == 'Z':
            point_total += 3

        if ((their_hand == 'A') and (my_hand == 'X')) or ((their_hand == 'B') and (my_hand == 'Y')) or ((their_hand == 'C') and (my_hand == 'Z')):
            point_total += 3
        elif ((their_hand == 'A') and (my_hand == 'Y')) or ((their_hand == 'B') and (my_hand == 'Z')) or ((their_hand == 'C') and (my_hand == 'X')):
            point_total += 6
        elif ((their_hand == 'A') and (my_hand == 'Z')) or ((their_hand == 'B') and (my_hand == 'X')) or ((their_hand == 'Y') and (my_hand == 'Z')):
            point_total += 0
    
    print('Point total is(PartOne):', point_total)
        
