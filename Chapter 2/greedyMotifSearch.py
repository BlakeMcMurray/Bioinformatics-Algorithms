import profileMostProb as pmp
import score
def greedy_motif_search(dna,k,t):
    best_motifs = []
    #assigns best_motifs to the first kmers
    for i in dna:
        best_motifs.append(i[0:k])
    

    #go through the first motif, assigning each kmer to motif
    for i in range(len(dna[0])-k+1):
        motif = dna[0][i:i+k]
        prof_motifs = []
        prof_motifs.append(motif)
        for j in range(1,t):
            prof = pmp.pm.profileMatrix(prof_motifs)
            nextKmer = pmp.profMostProb(dna[j],k,prof)
            prof_motifs.append(nextKmer)
        if(score.score(prof_motifs) < score.score(best_motifs)):
            best_motifs = prof_motifs
    return(best_motifs)
        
    



with open("in.txt","r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
f.close()

bm = greedy_motif_search(lines,12,25)

with open("out.txt","w") as f:
    for i in bm:
        f.write(i + "\n")
f.close()
