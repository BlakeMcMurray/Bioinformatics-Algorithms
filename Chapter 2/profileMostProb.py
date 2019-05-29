import profileMatrix as pm 
import letterMap as lm 
def profMostProb(Text,k,profile):
    mostProbKmer = Text[0:k]
    bestProb = 0
    prob = 1
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        for j in range(len(kmer)):
            index = lm.letterMap(kmer[j])
            prob = prob*profile[j][index]
        if(prob > bestProb):
            bestProb = prob
            mostProbKmer = kmer
        prob = 1
    return(mostProbKmer)
            

pseduoProf = []

'''with open("in.txt","r") as f:
    lines = f.readlines()
    Text = lines[0].strip()
    k = int(lines[1])
    for i in range(2,len(lines)):
        pseduoProf.append(lines[i].split())
f.close()

profile = []
for i in range(len(pseduoProf[0])):
    profile.append([])


for i in range(len(pseduoProf[0])):
    profile[i].append(float(pseduoProf[0][i]))
    profile[i].append(float(pseduoProf[1][i]))
    profile[i].append(float(pseduoProf[2][i]))
    profile[i].append(float(pseduoProf[3][i]))'''


#print(profMostProb(Text,k,profile))



   



