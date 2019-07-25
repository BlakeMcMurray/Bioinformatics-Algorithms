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

def min_skew(genome):
    skew_list = skew(genome)
    m = min(skew_list)
    min_skew = []
    for i in range(len(skew_list)):
        if(skew_list[i] == m):
            min_skew.append(i)
    return(min_skew)

print(min_skew("CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"))
    

        
