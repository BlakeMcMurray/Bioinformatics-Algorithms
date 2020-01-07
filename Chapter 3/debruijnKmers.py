import prefixSuffix as PS
def debruijn_kmers(kmers):
    graph = {}
    for i in kmers:
        if PS.prefix(i) not in graph:
            graph[PS.prefix(i)] = []
            graph[PS.prefix(i)].append(PS.suffix(i))
        else:
            graph[PS.prefix(i)].append(PS.suffix(i))
    return(graph)

f_in = open("input.txt","r")
kmers = f_in.readlines()
for i in range(len(kmers)):
    kmers[i] = kmers[i].strip()

graph = debruijn_kmers(kmers)
f_out = open("output.txt","w")

for i in graph:
    f_out.write(i + " -> ")
    for j in range(len(graph[i])):
        if(j == len(graph[i])-1):
            f_out.write(graph[i][j] + "\n")
        else:
            f_out.write(graph[i][j] + ", ")
            
f_out.close()

