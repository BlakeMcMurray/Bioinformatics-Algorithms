import profileMostProb as pmp 
def motifs(profile,Dna):
    kmers = []
    for i in Dna:
        kmers.append(pmp.profMostProb(i,len(profile),profile))
    return(kmers)
