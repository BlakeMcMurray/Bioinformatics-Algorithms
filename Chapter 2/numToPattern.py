import math
def numbertoPattern(num,k):
    pattern = []
    for i in reversed(range(0,k)):
        n = math.floor(num/(4**i))
        if(n == 0):
            pattern.append('A')
            continue
        elif(n == 1):
            pattern.append('C')
            num = num - 4**i
        elif(n == 2):
            pattern.append('G')
            num = num - 2*4**i
        elif(n == 3):
            pattern.append('T')
            num = num - 3*4**i

    toReturn = ''.join(pattern)
    return(toReturn)

