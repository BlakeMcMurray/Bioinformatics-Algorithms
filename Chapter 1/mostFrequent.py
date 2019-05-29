import math
import numpy
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


def patternToNumber(pattern):
    num = 0
    for i in reversed(range(len(pattern))):
        if(pattern[i] == "A"):
            num = num + 0*4**(len(pattern)-i-1)
        elif(pattern[i] == "C"):
            num = num + 1*4**(len(pattern)-i-1)
        elif(pattern[i] == "G"):
            num = num + 2*4**(len(pattern)-i-1)
        elif(pattern[i] == "T"):
            num = num + 3*4**(len(pattern)-i-1)
    return(num)

def mostFrequentBV(Text,k):
    lst = [0]*((4**k))
    words = []
    for i in range(len(Text)-k+1):
        lst[patternToNumber(Text[i:i+k])] += 1
    m = numpy.amax(lst,None)
    for i in range(len(lst)):
        if(lst[i] == m):
            words.append(numbertoPattern(i,k))

    return(words)



    


