import profileMostProb as pmp
import score
def greedyMotifSearch(Dna,k,t):
    bestMotifs = []
    #assigns bestMotifs to the first kmers
    for i in Dna:
        bestMotifs.append(i[0:k])
    

    #go through the first motif, assigning each kmer to motif
    for i in range(len(Dna[0])-k+1):
        motif = Dna[0][i:i+k]
        profMotifs = []
        profMotifs.append(motif)
        for j in range(1,t):
            prof = pmp.pm.profileMatrix(profMotifs)
            nextKmer = pmp.profMostProb(Dna[j],k,prof)
            profMotifs.append(nextKmer)
        if(score.score(profMotifs) < score.score(bestMotifs)):
            bestMotifs = profMotifs
    return(bestMotifs)
        
    



with open("in.txt","r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
f.close()

bm = greedyMotifSearch(lines,12,25)

with open("out.txt","w") as f:
    for i in bm:
        f.write(i + "\n")
f.close()  
