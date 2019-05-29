def hammingDist(st1,st2):
    dist = 0
    for i in range(len(st1)):
        if(st1[i] != st2[i]):
            dist += 1
    return(dist)

