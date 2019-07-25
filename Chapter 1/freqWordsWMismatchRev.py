import dNeighborhood as dNay
import mostFrequentSort as MFS
import approxPatMatch as aprx
import reverse_complement as rev
def freq_w_mismatch_rev(text,k,d):
   
    close = [0]*4**k
    freq = [0]*4**k
    patterns = []
    for i in range(len(text)-k+1):
        neigh = dNay.iterative_neighbors(text[i:i+k],d)
        for i in neigh:
            close[MFS.pattern_to_number(i)] = 1
            close[MFS.pattern_to_number(rev.reverse_comp(i))] = 1

    for i in range(len(close)):
        if(close[i] == 1):
            freq[i] = len(aprx.approx_match(MFS.number_to_pattern(i,k),text,d)) + len(aprx.approx_match(rev.reverse_comp(MFS.number_to_pattern(i,k)),text,d))

    m = max(freq)

    for i in range(len(freq)):
        if (freq[i] == m):
            patterns.append(MFS.number_to_pattern(i,k))
    return(patterns)



find = freq_w_mismatch_rev("AATCTGGCCGCGGCAATCTGGCCGCGGCCCGCGGCCCGCGGCCCGCGGCCCTCGAGTCCCGGAAATCTGGTCCCGGATCCCGGAAGGATCAAGCCTCGAGCCTCGAGTCCCGGACCGCGGCTCCCGGACCGCGGCTCCCGGAAGGATCAAGAATCTGGAGGATCAAGTCCCGGACCGCGGCAGGATCAAGTCCCGGAAGGATCAAGTCCCGGAAATCTGGCCTCGAGTCCCGGAAATCTGGTCCCGGACCTCGAGCCTCGAGCCTCGAGCCTCGAGAGGATCAAGCCGCGGCAGGATCAAGCCGCGGCCCTCGAGTCCCGGATCCCGGACCGCGGCAATCTGGAGGATCAAGCCGCGGCCCTCGAGAATCTGGCCTCGAGTCCCGGATCCCGGAAGGATCAAGTCCCGGATCCCGGAAGGATCAAGAATCTGGAATCTGGTCCCGGATCCCGGAAATCTGGAGGATCAAGCCTCGAGAATCTGGCCGCGGCAATCTGGAGGATCAAGAGGATCAAGAATCTGGCCGCGGCAGGATCAAGTCCCGGAAGGATCAAGTCCCGGATCCCGGAAGGATCAAGTCCCGGACCGCGGCAGGATCAAGAATCTGGAGGATCAAGTCCCGGACCTCGAGCCGCGGCTCCCGGACCTCGAGCCGCGGCTCCCGGATCCCGGAAATCTGGCCGCGGCAATCTGGAGGATCAAGTCCCGGATCCCGGACCGCGGCAGGATCAAGAGGATCAAGTCCCGGACCTCGAGCCGCGGCAGGATCAAGAATCTGGAGGATCAAGCCTCGAGCCTCGAGAGGATCAAGAATCTGGAATCTGGAGGATCAAGCCTCGAGTCCCGGA",5,3)


f = open("out.txt","w")
for i in find:
    f.write(i + " ")
