#working
import prefixSuffix as PS 
#constructs debruijn graph in O(n) (n = number of kmers)
def debruijn(text, k):
    graph = {}
    for i in range(len(text)-k+1):
        if PS.prefix(text[i:i+k]) not in graph:
            graph[PS.prefix(text[i:i+k])] = []
            graph[PS.prefix(text[i:i+k])].append(PS.suffix(text[i:i+k]))
        else:
            graph[PS.prefix(text[i:i+k])].append(PS.suffix(text[i:i+k]))
        
    return(graph)

    
text = "TTGCGTGTGGGGTCTAGTCACCTGGGGCCTATTTGATTGTCGCATGCTAAGGCTTATAGAGCACGAGTTCTTACAGAAACACGAGAGGTGCGCTAGCAAGCGAGCTCATTACGGGTACATCAGTCCCTCACGACAATTGCGTAATGGGGTCGCGACAGATAACCTCAATTTAGGTATGCACGTTAGATAGCGGTCCGATACACTAAGATCTGCTTAACCGCCACCCAAGACAGACACGTCAATAGAACGAATTGCATACATCGAGTCGGAGAGTGAAGGGATGCCATACCAAACGGTAGGAGTCTTCCTTCCGAGTTCCAGATCAACCAGGGGGGCAATCTGTCATAAAAGACACTTCCGACGGGACAACCCAACATGATTTAGCATAACCGTCGCACGATCGAACATACGCACGCTGTACGACCTCCGTAATAGGGGGTCCGCCCAGTCCGTAGCTAGTTGTGCAAAACTTCATCATAGACGTAGAGGCCACCCAGCATTCGTGCGAGTCCCCTAGTGCTGGGCGTTCTGCGGTTTTACTCGTTGTGAGGCCGCGCTACGTAAATGACGCGGTGCCAATTCCCCCCTATCTCCCGGACGATGTCCCAACCGCCACACTTCTGGACCGGTACGGGATAGTCGGTTTGGAGTGGCGTTTTGATTGCAGTATAGTCGCGCGTCTCAGGCGCAACGAGCTGTGACTCAAGGTCAGGCGCCCCTCGCATAAGACCTTCCCCACAACGCCAATTTGACCCCGTTCAGTGGTCGAATCTTACTCTCCACGTATTTCGAGAGGCCAACAGGCGGCGGTGCTCTTGGTGCCGGGCTCCTTCGCGAAATCGGGCTTCTGGCCGACAGGTTCTACGCCTGCGTATAATTTTGTCGTATAGTAGGTTCGCTGTCACAAACCTAGTCTTCTTGCTGACCGATTCCTGTCTTAGCATCAAGTTAACATCTATTGTAAGTTCGATAGTTATGTCCTGACTCCGTCTAGACGGCCCAGCAGTCTGCCGGTAGCAAGAGTTGGCTCTTCAAAGCGGCGGATAGGCTCAATCTCTCGGAAACCGCACCACTAGATTCTGCACCGCAGCGGGCTATCCACGCTCGTACCACCTCTTACGCGCCTCATGCACCGTATGATGCTCGGGATTAAGCCCAGTGCTAGAGAACTTGGGTAGTTCCTACCACTGCGGTATCTCATGTAGTATTTCTTATTTGCAGACGCATCTGGGTTACCACATTTAAATTGAGCTGCACTAGGCAGCTGAGACGTAAAACTACCGTGTGCTTAAAACCCCAGGTGAAGTCATGGGAAAGCCGCTACATTTCCTCATGCAATGCCCACCTTCGCTACACTATGTTAAGTTGTTCGGTGTACATCTCCTAGGACGGCTAGTTCGTTTTTGCAGGCCTTTGTATAAACTACCTAAAGTAGTGAGCTTAAGTTGCACTTTGTGTAATCCATGTCCCTCCCCAACCACGTCGCGAGAGTTCAGAGCGGATTGTTGTCTCACATAATAGGTCTTATCACCACATCTAGAAATCAGGCATTTTCCGCGGCCGTCCCCGACGCCCGATCGTCTCTCGGAAAAGATCCACATGTGCCCTTGACCACGCTCGCATGTATTTGCTCCTAGCTTGTGTTCAGTCGACCGTAGCGCATCGCGCCCGCACCTTAACGGAGCTGAGACGGCATACCGCTAGTGATCTCTTCGAGCGCAGGGGGTGTGAAGAGTCGATCTTTTATCAATCCCAGATGGAGGTTAAGTGGCTGGGTAGTGCTTACGAGGGAGCATGACTCATCTAGGAAGTCCCGGGCGATCCAAGATTCCGAGGCCAGGTGGGCTGATGGCGTGAGAAGCTAAATGTCATGATTGAGGTCTTGCAGCCAGGTGCGGTGATTACGGAGTGTTACATAGCCTAGTTTTGTAGCAAGAGCACCCTTCTGGAAGAGGCTACACAGGGTTCGACGCGGCCAATCCTCCCAAGCATCTTCCCCG"
graph = debruijn(text,12)

f_out = open("output.txt","w")
for i in graph:
    f_out.write(i + " -> ")
    for j in range(len(graph[i])):
        if(j == len(graph[i])-1):
            f_out.write(graph[i][j] + "\n")
        else:
            f_out.write(graph[i][j] + ", ")

f_out.close()
