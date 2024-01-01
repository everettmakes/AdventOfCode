f = list(map(str.strip, open("input3.txt", "r").readlines()))

valid = []
for y in range(len(f)):
    for x in range(len(f[y])):
        if not(str.isdigit(f[y][x])) and f[y][x] != '.':
            valid.append((x,y+1))
            valid.append((x,y-1))
            valid.append((x+1,y))
            valid.append((x-1,y))
            valid.append((x+1,y+1))
            valid.append((x-1,y-1))
            valid.append((x-1,y+1))
            valid.append((x+1,y-1))

total = 0
y=0
while y < len(f):
    x=0
    num = ''
    while x < len(f[y]):
        if str.isdigit(f[y][x]) and num == '':
            val = False
            while (x < len(f[y]) and str.isdigit(f[y][x])):
                num += f[y][x]
                if (x,y) in valid:
                    val = True
                x += 1
            if val == True:
                total += int(num)
            num = ''
            val = False
        x += 1
    y += 1
print(total)
        





