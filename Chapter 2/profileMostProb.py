import profileMatrix as pm 
import letterMap as lm 
def prof_most_prob(text,k,profile):
    most_prob_kmer = text[0:k]
    best_prob = 0
    prob = 1
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        for j in range(len(kmer)):
            index = lm.letter_map(kmer[j])
            prob = prob*profile[j][index]
        if(prob > best_prob):
            best_prob = prob
            most_prob_kmer = kmer
        prob = 1
    return(most_prob_kmer)
            








