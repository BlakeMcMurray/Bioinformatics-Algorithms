#working
import prefixSuffix as PS
#constructs overlap graph of a set of kmers
def overlap(kmers):
    o_graph = []
    for i in range(len(kmers)):
        o_graph.append([])

    for i in range(len(kmers)):
        for j in range(len(kmers)):
            if (i != j and PS.prefix(kmers[j]) == PS.suffix(kmers[i])):
                o_graph[i].append(kmers[j])

    return(o_graph)

f_in = open("input.txt","r")
kmers = f_in.readlines()
f_in.close()
s_kmers = []
for i in kmers:
    s_kmers.append(i.strip("\n"))
    

overlap = overlap(s_kmers)

f_out = open("output.txt","w")
for i in range(len(overlap)):
    if len(overlap[i]) != 0:
        f_out.write(s_kmers[i] + " -> " + overlap[i][0] + "\n")
f_out.close()
