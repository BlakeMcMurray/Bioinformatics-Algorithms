import hamming as ham
#return the kmer in Text that minimizes the hamming dist between
#pattern and kmer as well as the hamming dist
#-----working-----
def minD(Pattern,Text):
    k = len(Pattern)
    min = len(Pattern)
    kmer = ""
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        dist = ham.hammingDist(Pattern,kmer)
        if(dist < min):
            min = dist
    return(min)



