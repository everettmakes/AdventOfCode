import numpy as np
f = open('input4.txt', 'r')
lines = f.readlines()
data = [list(line.strip()) for line in lines]
data = np.array(data)

# generic
def findXMAS(d, x, y, dir):
    dx, dy = dir
    text = 'MAS'
    for t in text:
        if x < 0 or x > len(d[0, :]) - 1:
            return None
        if y < 0 or y > len(d[:, 0]) - 1:
            return None
        if d[y, x] != t:
            return None
        x += dx
        y += dy
    return (x-2*dx, y-2*dy)

a = {}
for y in range(len(data[:, 0])):
    for x in range(len(data[0, :])):
        result = []
        combs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        for comb in combs:
            xmas = findXMAS(data, x, y, comb)
            if xmas in a:
                a[xmas] += 1
            else:
                a[xmas] = 1
a[None] = 0
c = len([v for v in a.values() if v > 1])
print(c)