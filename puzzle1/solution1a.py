f = list(map(str.strip, open("input1.txt", "r").readlines()))

t=0

for l in f:
    s=0
    e=len(l)-1

    while not(str.isdigit(l[s])):
        s+=1
    while not(str.isdigit(l[e])):
        e-=1

    t = t + int(l[s] + l[e])

print(t)
