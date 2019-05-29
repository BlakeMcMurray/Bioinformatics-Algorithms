import dNeighborhood
import mostFrequentSort
def findFreqWMisMatch(Text,k,d):
    FreqPatterns = []
    Neighborhoods = []
    patterns = []
    for i in range(len(Text)-k+1):
        neigh = dNeighborhood.iterativeNeighbors(Text[i:i+k],d)
        for i in neigh:
            Neighborhoods.append(i)
   
    for i in Neighborhoods:
        FreqPatterns.append(mostFrequentSort.patternToNumber(i))
    
    count = [1]*len(FreqPatterns)
    FreqPatterns = sorted(FreqPatterns)

    for i in range(0,len(FreqPatterns)-1):
        if(FreqPatterns[i] == FreqPatterns[i+1]):
            count[i+1] = count[i]+1
    m = max(count)
    x = sum(count)
    print(x)
    for i in range(len(count)):
        if(count[i] == m):
            print(i)
    for i in range(len(count)):
        if(count[i] == m):
            patterns.append(mostFrequentSort.numbertoPattern(FreqPatterns[i],k))
            print(mostFrequentSort.numbertoPattern(FreqPatterns[i],k))
    return(patterns)

find = findFreqWMisMatch("CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC",10,2)

f = open("out.txt","w")
for i in find:
    f.write(i + " ")