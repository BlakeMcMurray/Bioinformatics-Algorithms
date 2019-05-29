#working (probably)
import countMatrix as CM
#calculates the score of a set of motifs
#breaks ties by first encounter of max nucleotide
def score(kmers):
    countM = CM.count(kmers)
    m = 0
    score = 0
    tracker = 0
    for i in range(len(countM)):
        m = max(countM[i])
        for j in range(len(countM[i])):
            if countM[i][j] == m and tracker == 0:
                tracker = 1
                continue
            else:
                score += countM[i][j]
        tracker = 0
    return(score)

    


