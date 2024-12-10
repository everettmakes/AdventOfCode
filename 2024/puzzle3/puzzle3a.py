f = open('input3.txt', 'r')
data = f.read()
print(data)
import numpy as np

def digit(s, i):
    x = ''
    while i < len(s) and s[i].isdigit():
        x += s[i]
        i += 1
    return x, i

def select(s):
    vals = []
    i = 0
    while i < len(s):
        if i + 4 <= len(s) and s[i:i+4] == 'mul(':
            i += 4
        else:
            i += 1
            continue

        d1, i = digit(s, i)
        if not d1:
            continue

        if i < len(s) and s[i] == ',':
            i += 1
        else:
            continue

        d2, i = digit(s, i)
        if not d2:
            continue

        if i < len(s) and s[i] == ')':
            i += 1
        else:
            continue

        vals.append([int(d1), int(d2)])
    return vals

print(np.sum(np.prod(select(data), axis=1)))
