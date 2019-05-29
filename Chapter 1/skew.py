def skew(genome):
    lst = [0]*(len(genome)+1)
    for i in range(1,len(lst)):
        if(genome[i-1] == "A" or genome[i-1] == "T"):
            lst[i] = lst[i-1]
        elif(genome[i-1] == "G"):
            lst[i] = lst[i-1]+1
        elif(genome[i-1] == "C"):
            lst[i] = lst[i-1]-1
    return(lst)

def minSkew(genome):
    skewList = skew(genome)
    m = min(skewList)
    minSkew = []
    for i in range(len(skewList)):
        if(skewList[i] == m):
            minSkew.append(i)
    return(minSkew)

print(minSkew("CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"))
    

        
