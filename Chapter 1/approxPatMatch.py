import hamming
#Working code
def approxMatch(Pattern,Text,d):
    sPositions = []
    for i in range(len(Text)-len(Pattern)+1):
        if(hamming.hammingDist(Pattern,Text[i:i+len(Pattern)]) <= d):
            sPositions.append(i)
    return(sPositions)



