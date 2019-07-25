def pattern_to_number(pattern):
    num = 0
    for i in reversed(range(len(pattern))):
        if(pattern[i] == "A"):
            num = num + 0*4**(len(pattern)-i-1)
        elif(pattern[i] == "C"):
            num = num + 1*4**(len(pattern)-i-1)
        elif(pattern[i] == "G"):
            num = num + 2*4**(len(pattern)-i-1)
        elif(pattern[i] == "T"):
            num = num + 3*4**(len(pattern)-i-1)
    return(num)
