def pattern_match(pattern,text):
    for i in range(len(text)-len(pattern)+1):
        if(text[i:i+len(pattern)] == pattern):
            return(True)
    return(False)
