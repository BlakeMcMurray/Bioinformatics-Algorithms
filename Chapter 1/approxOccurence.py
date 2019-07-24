import hamming as ham
def approx_occurence(text,pattern,d):
    for i in range(len(text)-len(pattern)+1):
        if(ham.hammingDist(pattern,text[i:i+len(pattern)]) <= d):
            return(True)
    return(False)
