def hamming_dist(st_1,st_2):
    dist = 0
    for i in range(len(st_1)):
        if(st_1[i] != st_2[i]):
            dist += 1
    return(dist)
