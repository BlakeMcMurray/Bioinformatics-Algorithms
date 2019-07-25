import hamming
#Working code
def approx_match(pattern,text,d):
    s_positions = []
    for i in range(len(text)-len(pattern)+1):
        if(hamming.hamming_dist(pattern,text[i:i+len(pattern)]) <= d):
            s_positions.append(i)
    return(s_positions)
