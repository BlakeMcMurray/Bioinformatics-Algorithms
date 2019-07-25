import math
import numpy
def number_to_pattern(num,k):
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
    s_pattern = ''.join(pattern)
    return(s_pattern)


def pattern_to_number(pattern):
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

def most_frequent_bv(text,k):
    lst = [0]*((4**k))
    words = []
    for i in range(len(text)-k+1):
        lst[pattern_to_number(text[i:i+k])] += 1
    m = numpy.amax(lst,None)
    for i in range(len(lst)):
        if(lst[i] == m):
            words.append(number_to_pattern(i,k))

    return(words)
