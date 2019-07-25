import pseudoCountMatrix as CM 
#working 
def profile_matrix(motifs):
    count_m = CM.count(motifs)
    profile = count_m/2*(len(motifs))
    return(profile)
