    
import hamming as ham
#return the kmer in text that minimizes the hamming dist between
#pattern and kmer as well as the hamming dist
#-----working-----
def min_d(pattern,text):
    k = len(pattern)
    min = len(pattern)
    kmer = ""
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        dist = ham.hamming_dist(pattern,kmer)
        if(dist < min):
            min = dist
    return(min)
