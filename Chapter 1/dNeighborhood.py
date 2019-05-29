#Working code
def immediateNeighbors(Pattern):
    Neighborhood = []
    Neighborhood.append(Pattern)
    letters = ["A","C","G","T"]
    for i in range(len(Pattern)):
        k = Pattern[i]
        for j in letters:
            if(j != k):
                toAdd = list(Pattern)
                toAdd[i] = j
                Neighborhood.append(''.join(toAdd))
    return(Neighborhood)

def iterativeNeighbors(Pattern,d):
    Neighborhood = [Pattern]
    m = 0
    for j in range(0,d):
        for i in Neighborhood:
            if(m == d):
                break
            immNeigh = immediateNeighbors(i)
            for k in immNeigh:
                Neighborhood.append(k)
            Neighborhood = list(dict.fromkeys(Neighborhood))
            m += 1 
    return(Neighborhood)
