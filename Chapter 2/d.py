import minD
#working
#returns the minimum score + the motifs that give the min score
def d(pattern,motifs):
    summ = 0
    for i in motifs:
        d_call = minD.minD(pattern,i)
        summ += d_call        
    return(summ)
