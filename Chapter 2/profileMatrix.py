import pseudoCountMatrix as CM 
#working 
def profileMatrix(Motifs):
    countM = CM.count(Motifs)
    profile = countM/2*(len(Motifs))
    return(profile)

