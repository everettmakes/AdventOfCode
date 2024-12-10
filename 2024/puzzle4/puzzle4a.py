import numpy as np
f = open('input4.txt', 'r')
lines = f.readlines()
data = [list(line.strip()) for line in lines]
data = np.array(data)

# generic
def findXMAS(d, x, y, dx, dy):
    text = 'XMAS'
    for t in text:
        if x < 0 or x > len(d[0, :]) - 1:
            return 0
        if y < 0 or y > len(d[:, 0]) - 1:
            return 0
        if d[y, x] != t:
            return 0
        x += dx
        y += dy
    return 1


total = 0
for y in range(len(data[:, 0])):
    for x in range(len(data[0, :])):
        result = []
        # vertical
        result.append(findXMAS(data, x, y, 0, 1))
        result.append(findXMAS(data, x, y, 0, -1))

        # horizontal
        result.append(findXMAS(data, x, y, 1, 0))
        result.append(findXMAS(data, x, y, -1, 0))

        # diagonal
        result.append(findXMAS(data, x, y, 1, 1))
        result.append(findXMAS(data, x, y, 1, -1))
        result.append(findXMAS(data, x, y, -1, 1))
        result.append(findXMAS(data, x, y, -1, -1))
        total += np.sum(result)
print(total)
