#working
#generates kmer comp of a string text
#returns in lexicographic order because in practice, order is not known.
def composition(text,k):
    kmer_comp = []
    for i in range(len(text)-k+1):
        kmer_comp.append(text[i:i+k])
    return(kmer_comp)

f_in = open("input.txt","r")
k = int(f_in.readline())
text = f_in.readline()
comp = composition(text,k)
f_in.close()

f_out = open("output.txt","w")
for i in comp:
    f_out.write(i + "\n")
f_out.close()



