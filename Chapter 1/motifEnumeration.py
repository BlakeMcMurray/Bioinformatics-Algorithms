import dNeighborhood as dN
import approxOccurence as AO
def motifEnumeration(Dna,k,d):
    patterns = []
    count = 1
    for i in range(len(Dna[0])-k+1):
        kmer = Dna[0][i:i+k]
        neigh = dN.iterativeNeighbors(kmer,d)
        for p in neigh:
            for m in range(1,len(Dna)):
                if AO.approxOccurence(Dna[m],p,d) == False:
                    count = 0
                    break
            
            if(count == 1):
                patterns.append(p)
            count = 1
    patterns = list(dict.fromkeys(patterns))
    return(patterns)


print(motifEnumeration(['TGTCCGTTCAGGAGTGAACTTCGAG','TCCTGTATCCATTTAAGTCGGCCCT','GCTATTATACTCGTTACCTGTTTCC','CCAAGTATCCAGTGTTTGTATTGTC','ACGAATGTCCGGCTGAAGCGATCTA','TTTCCTTTACTACACCAAACGCGAT','TGTCCCCCGGCTTTATCTTCGTCTG','TTTCCAGTTTCTATGGTTGTGCTAG','GTAGCTACCTTTCGGTCTCCCAGGG','TGGGATCTCCAAGTCCCATCGTATT'],5,1))

                
            


