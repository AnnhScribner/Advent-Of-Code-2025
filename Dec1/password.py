NUMBER_OF_DIAL_DIGITS = 100
START = 50

"""
Part One
"""

position = START # the dial starts at 50
count = 0

with open('Dec1/rotations.txt', 'r') as file:
    lines = file.readlines()
    direction = ''
    moves = 0
    
    for line in lines:
        l = line.strip()
        direction = l[0] # get direction L/R
        moves = int(l[1:]) # get the quantity of moviments 
        
        if direction == 'R': # goes to the right, adding moves to start
            position = (position + moves) % NUMBER_OF_DIAL_DIGITS
        elif direction == 'L': # goes to the left, subtracting moves from start
            position = (position - moves) % NUMBER_OF_DIAL_DIGITS

        if position == 0:
            count += 1

print(count) # this is the password for part 1 for the chalange 1 for Dec 1, 2025
