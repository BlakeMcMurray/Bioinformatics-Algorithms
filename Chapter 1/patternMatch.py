def patternMatch(Pattern,Text):
    for i in range(len(Text)-len(Pattern)+1):
        if(Text[i:i+len(Pattern)] == Pattern):
            return(True)
    return(False)