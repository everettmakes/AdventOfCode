import numpy as np
f = open('input6.txt', 'r')
lines = f.readlines()
data = [list(line.strip()) for line in lines]
data = np.array(data)

old_guard = np.where(data == '^')
guard = tuple((old_guard[0][0], old_guard[1][0]))
dir = tuple((-1, 0))
transition = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
visited = set()

height = len(data[:, 0])
width = len(data[0, :])

while guard[0] < height and guard[1] < width and guard[0] >= 0 and guard[1] >= 0:
    visited.add(guard)
    nxt = tuple((guard[0] + dir[0], guard[1] + dir[1]))
    if nxt[0] < height and nxt[0] >= 0 and nxt[1] >= 0 and nxt[1] < width and data[nxt] == '#':
        dir = transition[dir]
        data[guard] = '>'
    else:
        guard = nxt
print(len(visited))