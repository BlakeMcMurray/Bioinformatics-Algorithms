import d
import numToPattern as ntp  
import patToNumber as ptn 
import math
#working
def medianString(Dna,k):
    dist = math.inf
    pattern = ""
    for i in range(4**k):
        kmer = ntp.numbertoPattern(i,k)
        num = d.d(kmer,Dna)
        if(dist > num):
            dist = num
            pattern = kmer
    return(pattern)

inFile = open("in.txt","r")
mylist = [line.rstrip('\n') for line in inFile]
k = int(mylist[0])
Dna = []
for i in range(1,len(mylist)):
    Dna.append(mylist[i])


print(medianString(Dna,k))


        
    
        