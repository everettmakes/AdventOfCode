import numpy as np
f = open('input1.txt', 'r')
lines = [line.strip().split() for line in f.readlines()]
data = np.array(lines)
r1 = np.sort(data[:, 0].astype(int))
r2 = np.sort(data[:, 1].astype(int))

score = 0
for item in r1:
    score += len(np.where(r2 == item)[0]) * item
print(score)