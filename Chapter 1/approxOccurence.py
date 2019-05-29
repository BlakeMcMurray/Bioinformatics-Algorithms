import hamming
def approxOccurence(Text,Pattern,d):
    for i in range(len(Text)-len(Pattern)+1):
        if(hamming.hammingDist(Pattern,Text[i:i+len(Pattern)]) <= d):
            return(True)
    return(False)
