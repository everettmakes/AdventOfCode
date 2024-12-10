import numpy as np
f = open('input2.txt', 'r')
lines = [line.strip().split() for line in f.readlines()]
safe = 0

def isValid(row, s): # s = sign [-1, 1]
    prev = row[0]
    for val in row[1:]:
        l = prev + (1 * s)
        r = prev + (3 * s)
        if s > 0 and val >= l and val <= r:
            pass
        elif val <= l and val >= r:
             pass
        else:
            return False
        prev = val
    return True

safe = 0
for row in lines:
    row = np.array(row).astype(int)
    up = isValid(row, 1)
    down = isValid(row, -1)
    if up or down:
        safe += 1
print(safe)

