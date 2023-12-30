f = list(map(str.strip, open("input2.txt", "r").readlines()))

def processLn(l):
    config = {"red": 0, "green": 0, "blue": 0}
    id, data = l.split(":")
    _, id = id.split(" ")
    data = data.split(";")
    for set in data:
        set = set.split(",")
        for item in set:
            _, num, col = item.split(" ")
            if (config[col] < int(num)): config[col] = int(num)
    return (config['red'] * config['green'] * config['blue'])

t = 0
for l in f:
    t = t + processLn(l)
print(t)