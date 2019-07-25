import d
import numToPattern as ntp  
import patToNumber as ptn 
import math
#working
def median_string(dna,k):
    dist = math.inf
    pattern = ""
    for i in range(4**k):
        kmer = ntp.number_to_pattern(i,k)
        num = d.d(kmer,dna)
        if(dist > num):
            dist = num
            pattern = kmer
    return(pattern)

in_file = open("in.txt","r")
my_list = [line.rstrip('\n') for line in in_file]
k = int(my_list[0])
dna = []
for i in range(1,len(my_list)):
    dna.append(my_list[i])


print(median_string(dna,k))
