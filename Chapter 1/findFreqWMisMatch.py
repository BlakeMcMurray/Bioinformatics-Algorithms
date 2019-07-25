import dNeighborhood
import mostFrequentSort
def find_freq_w_mismatch(text,k,d):
    freq_patterns = []
    neighborhoods = []
    patterns = []
    for i in range(len(text)-k+1):
        neigh = dNeighborhood.iterative_neighbors(text[i:i+k],d)
        for i in neigh:
            neighborhoods.append(i)
   
    for i in neighborhoods:
        freq_patterns.append(mostFrequentSort.pattern_to_number(i))
    
    count = [1]*len(freq_patterns)
    freq_patterns = sorted(freq_patterns)

    for i in range(0,len(freq_patterns)-1):
        if(freq_patterns[i] == freq_patterns[i+1]):
            count[i+1] = count[i]+1

    m = max(count)
    x = sum(count)

    for i in range(len(count)):
        if(count[i] == m):
            print(i)
    for i in range(len(count)):
        if(count[i] == m):
            patterns.append(mostFrequentSort.number_to_pattern(freq_patterns[i],k))
    return(patterns)

find = find_freq_w_mismatch("CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC",10,2)

f = open("out.txt","w")
for i in find:
    f.write(i + " ")
