import dNeighborhood
import mostFrequentSort
import approxPatMatch
def find_freq_mismatch(text,k,d):
    close = [0]*4**k
    freq = [0]*4**k
    patterns = []
    for i in range(len(text)-k+1):
        neigh = dNeighborhood.iterative_neighbors(text[i:i+k],d)
        for i in neigh:
            close[mostFrequentSort.pattern_to_number(i)] = 1
    for i in range(len(close)):
        if(close[i] == 1):
            freq[i] = len(approxPatMatch.approx_match(mostFrequentSort.number_to_pattern(i,k),text,d))

    m = max(freq)
    x = sum(freq)

    for i in range(len(freq)):
        if (freq[i] == m):
            patterns.append(mostFrequentSort.number_to_pattern(i,k))
            print(mostFrequentSort.number_to_pattern(i,k))
    return(patterns)

find = find_freq_mismatch("CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC",10,2)

f = open("out.txt","w")
for i in find:
    f.write(i + " ")
