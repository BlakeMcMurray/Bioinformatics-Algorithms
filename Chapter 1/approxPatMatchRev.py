import hamming
import reverseComplement
def approxPatMatchRev(Pattern,Text,d):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if(hamming.hammingDist(Text[i:i+len(Pattern)],Pattern) <= d or hamming.hammingDist(Text[i:i+len(Pattern)],reverseComplement.reverseComp(Pattern)) <= d):
            count = count + 1
    return(count)
