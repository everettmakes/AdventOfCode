f = open('input5.txt', 'r')
lines = f.read().splitlines()

#dependencies 
d = {} # val : vals that must come AFTER val

l = 1
for line in lines:
    if line == '':
        break
    d1, d2 = line.split("|")
    if d1 in d:
        d1 = d[d1].append(d2)
    else:
        d[d1] = [d2]
    l += 1

def validLine(line):
    for i in range(len(line)-1):
        # for each item
        for j in range(i, len(line)):
            # check if items after have to come before it.
            if line[j] in d and line[i] in d[line[j]]:
                return False
    return True

def updateLine(line):
    newLine = line
    for i in range(len(line)-1):
        # for each item
        for j in range(i, len(line)):
            # check if items after have to come before it.
            if line[j] in d and line[i] in d[line[j]]:
                temp = line[j]
                line[j] = line[i]
                line[i] = temp
    return newLine

total = 0
for line in lines[l:]:
    line = line.split(",")
    if not validLine(line):
        newLine = line
        while not validLine(newLine):
            newLine = updateLine(newLine)
        total += int(newLine[len(newLine) // 2])
print(total)