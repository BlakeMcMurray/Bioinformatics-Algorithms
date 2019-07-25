import dNeighborhood as dN
import approx_occurence as AO
def motif_enumeration(dna,k,d):
    patterns = []
    count = 1
    for i in range(len(dna[0])-k+1):
        kmer = dna[0][i:i+k]
        neigh = dN.iterative_neighbors(kmer,d)
        for p in neigh:
            for m in range(1,len(dna)):
                if AO.approx_occurence(dna[m],p,d) == False:
                    count = 0
                    break
            
            if(count == 1):
                patterns.append(p)
            count = 1
    patterns = list(dict.fromkeys(patterns))
    return(patterns)


print(motif_enumeration(['TGTCCGTTCAGGAGTGAACTTCGAG','TCCTGTATCCATTTAAGTCGGCCCT','GCTATTATACTCGTTACCTGTTTCC','CCAAGTATCCAGTGTTTGTATTGTC','ACGAATGTCCGGCTGAAGCGATCTA','TTTCCTTTACTACACCAAACGCGAT','TGTCCCCCGGCTTTATCTTCGTCTG','TTTCCAGTTTCTATGGTTGTGCTAG','GTAGCTACCTTTCGGTCTCCCAGGG','TGGGATCTCCAAGTCCCATCGTATT'],5,1))

                
            


