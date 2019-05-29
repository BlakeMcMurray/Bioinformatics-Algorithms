#working
import numpy
def count(motifs):
    count = numpy.ones((len(motifs[0]),4))
    for j in range(len(motifs[0])):    
        for i in range(len(motifs)):
            if motifs[i][j] == "A":
                count[j,0] += 1
            if motifs[i][j] == "C":
                count[j,1] += 1
            if motifs[i][j] == "G":
                count[j,2] += 1
            if motifs[i][j] == "T":
                count[j,3] += 1
    return(count)



    
