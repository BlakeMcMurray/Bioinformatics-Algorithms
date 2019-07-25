#working (probably)
import countMatrix as CM
#calculates the score of a set of motifs
#breaks ties by first encounter of max nucleotide
def score(kmers):
    count_m = CM.count(kmers)
    m = 0
    score = 0
    tracker = 0
    for i in range(len(count_m)):
        m = max(count_m[i])
        for j in range(len(count_m[i])):
            if count_m[i][j] == m and tracker == 0:
                tracker = 1
                continue
            else:
                score += count_m[i][j]
        tracker = 0
    return(score)
