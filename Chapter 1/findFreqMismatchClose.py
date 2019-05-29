import dNeighborhood
import mostFrequentSort
import approxPatMatch
def findFreqMismatch(Text,k,d):
    close = [0]*4**k
    freq = [0]*4**k
    patterns = []
    for i in range(len(Text)-k+1):
        neigh = dNeighborhood.iterativeNeighbors(Text[i:i+k],d)
        for i in neigh:
            close[mostFrequentSort.patternToNumber(i)] = 1
    for i in range(len(close)):
        if(close[i] == 1):
            freq[i] = len(approxPatMatch.approxMatch(mostFrequentSort.numbertoPattern(i,k),Text,d))

    m = max(freq)
    x = sum(freq)
    print(x)
    for i in range(len(freq)):
        if (freq[i] == m):
            patterns.append(mostFrequentSort.numbertoPattern(i,k))
            print(mostFrequentSort.numbertoPattern(i,k))
    return(patterns)

find = findFreqMismatch("CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC",10,2)

f = open("out.txt","w")
for i in find:
    f.write(i + " ")