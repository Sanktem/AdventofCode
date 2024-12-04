#Advent of Code Day 2
#A, B, C is their choice, and X(1), Y(2), Z(3), is mine
#win(6), lose(0), draw(3)
#X is lose, Y is draw, Z is win

#vars
# win_match = 6
# lose_match = 0
# draw_match = 3

with open ('/home/sanktem/Desktop/Scripting/AdventofCode/Day2/data.txt', 'r') as f:
    line = f.readlines()
    point_total = 0
    for match in line:
        their_hand = match[0].strip()
        my_hand = match[2].strip()

        if ((their_hand == 'A') and (my_hand == 'X')):
            #lose pick sissors
            point_total += 3
        elif ((their_hand == 'B') and (my_hand == 'X')):
            #lose pick Rock
            point_total += 1
        elif ((their_hand == 'C') and (my_hand == 'X')):
            #lose pick Paper
            point_total += 2
        elif ((their_hand == 'A') and (my_hand == 'Y')):
            #draw pick Rock
            point_total += 4
        elif ((their_hand == 'B') and (my_hand == 'Y')):
            #draw pick Paper
            point_total += 5
        elif ((their_hand == 'C') and (my_hand == 'Y')):
            #draw pick Sissors
            point_total += 6
        elif ((their_hand == 'A') and (my_hand == 'Z')):
            #win pick paper
            point_total += 8
        elif ((their_hand == 'B') and (my_hand == 'Z')):
            #win pick sissors
            point_total += 9
        elif ((their_hand == 'C') and (my_hand == 'Z')):
            #win pick rock
            point_total += 7
    
    print('Point total is(PartTwo):', point_total)
        
