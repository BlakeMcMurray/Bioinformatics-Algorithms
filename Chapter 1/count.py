def Count(Text,subString):
    count = 0
    for i in range(len(Text)-len(subString)+1):
        if(Text[i:i+len(subString)] == subString):
            count = count + 1
    return(count)



