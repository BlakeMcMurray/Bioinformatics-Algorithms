import minD
#working
#returns the minimum score + the motifs that give the min score
def d(Pattern,Motifs):
    sum = 0
    for i in Motifs:
        dCall = minD.minD(Pattern,i)
        sum += dCall        
    return(sum)
