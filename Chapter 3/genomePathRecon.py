#working
#reconstructs string from genome path
def genome_path_recon(kmers):
    start = kmers[0]
    for i in range(1,len(kmers)):
        start = start + kmers[i][len(kmers[i])-1]
    return(start)

f_in = open("input.txt","r")
kmers = f_in.readlines()
f_in.close()
s_kmers = []
for i in kmers:
    s_kmers.append(i.strip("\n"))
    

genome = genome_path_recon(s_kmers)

f_out = open("output.txt","w")
f_out.write(genome)
f_out.close()

