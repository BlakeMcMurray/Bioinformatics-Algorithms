#Working code
def immediate_neighbors(pattern):
    neighborhood = []
    neighborhood.append(pattern)
    letters = ["A","C","G","T"]
    for i in range(len(pattern)):
        k = pattern[i]
        for j in letters:
            if(j != k):
                toAdd = list(pattern)
                toAdd[i] = j
                neighborhood.append(''.join(toAdd))
    return(neighborhood)

def iterative_neighbors(pattern,d):
    neighborhood = [pattern]
    m = 0
    for j in range(0,d):
        for i in neighborhood:
            if(m == d):
                break
            imm_neigh = immediate_neighbors(i)
            for k in imm_neigh:
                neighborhood.append(k)
            neighborhood = list(dict.fromkeys(neighborhood))
            m += 1 
    return(neighborhood)
