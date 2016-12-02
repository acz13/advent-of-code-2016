KEYPAD1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
KEYPAD2 = [(0,   0,   1,   0,  0),
           (0,   2,   3,   4,  0),
           (5,   6,   7,   8,  9),
           (0,  'A', 'B', 'C', 0),
           (0,   0,  'D',  0,  0)]
x1, y1 = 1, 1
x2, y2 = 0, 2
INSTRUCTIONS = {"U": (0, -1), "D": (0, 1),
         "L": (-1, 0), "R": (1, 0)}
with open("day2.input") as f:
    for i in f:
        for k in i.strip():
            ins = INSTRUCTIONS[k]
            x1 = max(0, min(x1 + ins[0], 2)) # Idea from a friend
            y1 = max(0, min(y1 + ins[1], 2))

            x2n = max(0, min(x2 + ins[0], 4))
            y2n = max(0, min(y2 + ins[1], 4))
            if KEYPAD2[y2n][x2n]:
                x2, y2 = x2n, y2n
        else:
            print(KEYPAD1[y1][x1], KEYPAD2[y2][x2])
    else:
        print()