f = list(map(str.strip, open("input2.txt", "r").readlines()))

def processLn(l):
    config = {"red": 12, "green": 13, "blue": 14}
    id, data = l.split(":")
    _, id = id.split(" ")
    data = data.split(";")
    for set in data:
        set = set.split(",")
        for item in set:
            _, num, col = item.split(" ")
            if (config[col] < int(num)): return 0
    return int(id)

t = 0
for l in f:
    t = t + processLn(l)
print(t)