"""
I wrote this pretty much as soon as I got out of bed... uploaded at school
Edited for readability in the afternoon
Commented pretty much every line XD
"""

# Manhattan distance (Take absolute values and add)
man = lambda x: abs(x[0]) + abs(x[1])
# Places we have been to already. Start with (0, 0) in case we run over it
been = [(0, 0)]
# 0 North, 1 East, etc. Each direction is an int storing how many blocks we have gone in that direction
directions = [0] * 4
# List index of "directions"
face = 0
# Have we found the first duplication?
part_two = False

with open("day1.input") as f:
    lst = f.read().strip().split(', ')

for k in lst:
    if k[0] == 'L':
        # If we turn left we want to subtract 1. i.e. 0 => -1 => 3 = West
        face = (face - 1) % 4
    else:
        # Same here but +1 and to the right
        face = (face + 1) % 4
    # We want to run an iterator on the number of blocks we run and increment in case we run over the duplication in the middle
    for _ in range(int(k[1:])):
        # Increment whatever direction we are facing by 1
        directions[face] += 1
        # East - West (1-3), North - South (0-2)
        loc = (directions[1] - directions[3], directions[0] - directions[2])
        # Have we been here before?
        if loc in been and not part_two:
            print("P2:", man(loc))
            part_two = True
        # Add location to places we've been
        been.append(loc)
else:
    # When we're done take the Manhattan distance of our final destination!
    print("P1:", man(been[-1]))
