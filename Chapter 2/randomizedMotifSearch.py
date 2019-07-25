import motifs
import random
import score
#working
def randomized_motif_search(dna,k,t):
    kmers = []
    for i in dna:
        r = random.randint(0,len(i)-k)
        kmers.append(i[r:r+k])
    while(True):
        prof = motifs.pmp.pm.profile_matrix(kmers)
        n_kmers = motifs.motifs(prof,dna)
        if(score.score(n_kmers) < score.score(kmers)):
            kmers = n_kmers
        else:
            return(kmers)

def randomized_motif_search1000(dna,k,t):
    kmers = []
    for i in dna:
        r = random.randint(0,len(i)-k+1)
        kmers.append(i[r:r+k])

    for i in range(1000):
        n_kmers = randomized_motif_search(dna,k,t)
        if(score.score(n_kmers) < score.score(kmers)):
            kmers = n_kmers
    return(kmers)

with open("in.txt","r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
f.close()

rand = randomized_motif_search1000(lines,15,20)

with open("out.txt","w") as f:
    for i in rand:
        f.write(i + "\n")
f.close()  
