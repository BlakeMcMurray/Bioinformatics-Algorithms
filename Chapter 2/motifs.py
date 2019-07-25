import profileMostProb as pmp 
def motifs(profile,dna):
    kmers = []
    for i in dna:
        kmers.append(pmp.prof_most_prob(i,len(profile),profile))
    return(kmers)
