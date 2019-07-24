import hamming
#Working code
def approx_match(pattern,text,d):
    sPositions = []
    for i in range(len(text)-len(pattern)+1):
        if(hamming.hammingDist(pattern,text[i:i+len(pattern)]) <= d):
            sPositions.append(i)
    return(sPositions)


