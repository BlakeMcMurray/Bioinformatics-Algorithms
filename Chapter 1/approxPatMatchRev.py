import hamming
import reverseComplement as RC
def approx_pat_match_rev(pattern,text,d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if(hamming.hamming_dist(text[i:i+len(pattern)],pattern) <= d or hamming.hamming_dist(text[i:i+len(pattern)],RC.reverse_comp(pattern)) <= d):
            count = count + 1
    return(count)
