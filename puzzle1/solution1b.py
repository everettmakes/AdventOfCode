f = list(map(str.strip, open("input1.txt", "r").readlines()))          

# -- takes in line l and index i. if i... is in digits then true
def isDigit(i, l):

    #array of digits
    digits={"one":1, "two":2, "three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

    #loop through possible letter combinations
    for x in range(len(l)-i+1):
        if l[i:i+x] in digits:
            return digits[l[i:i+x]]     
        
    #if its a digit..
    if str.isdigit(l[i]):
        return int(l[i])
    
    return -1

t=0
for l in f:
    s=0
    e=len(l)-1

    while (isDigit(s, l) < 0):
        s+=1
    s=isDigit(s, l)

    while (isDigit(e, l) < 0):
        e-=1
    e=isDigit(e, l)

    print(int(str(s) + str(e)))
    t = t + int(str(s) + str(e))


print(t)
