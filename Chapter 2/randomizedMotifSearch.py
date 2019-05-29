import motifs
import random
import score
#working
def randomizedMotifSearch(Dna,k,t):
    kmers = []
    for i in Dna:
        r = random.randint(0,len(i)-k)
        kmers.append(i[r:r+k])
    while(True):
        prof = motifs.pmp.pm.profileMatrix(kmers)
        nKmers = motifs.motifs(prof,Dna)
        if(score.score(nKmers) < score.score(kmers)):
            kmers = nKmers
        else:
            return(kmers)

def randomizedMotifSearch1000(Dna,k,t):
    kmers = []
    for i in Dna:
        r = random.randint(0,len(i)-k+1)
        kmers.append(i[r:r+k])

    for i in range(1000):
        nKmers = randomizedMotifSearch(Dna,k,t)
        if(score.score(nKmers) < score.score(kmers)):
            kmers = nKmers
    return(kmers)

with open("in.txt","r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
f.close()

rand = randomizedMotifSearch1000(lines,15,20)

with open("out.txt","w") as f:
    for i in rand:
        f.write(i + "\n")
f.close()  




