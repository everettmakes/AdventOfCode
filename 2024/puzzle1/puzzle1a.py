import numpy as np
f = open('input1.txt', 'r')
lines = [line.strip().split() for line in f.readlines()]
data = np.array(lines)
r1 = np.sort(data[:, 0].astype(int))
r2 = np.sort(data[:, 1].astype(int))
s = abs(r1 - r2)
print(sum(s))
