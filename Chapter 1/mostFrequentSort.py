import math
import numpy
def number_to_pattern(num,k):
    pattern = []
    for i in reversed(range(0,k)):
        n = math.floor(num/(4**i))
        if(n == 0):
            pattern.append('A')
            continue
        elif(n == 1):
            pattern.append('C')
            num = num - 4**i
        elif(n == 2):
            pattern.append('G')
            num = num - 2*4**i
        elif(n == 3):
            pattern.append('T')
            num = num - 3*4**i
    s_pattern = ''.join(pattern)
    return(s_pattern)


def pattern_to_number(pattern):
    num = 0
    for i in reversed(range(len(pattern))):
        if(pattern[i] == "A"):
            num = num + 0*4**(len(pattern)-i-1)
        elif(pattern[i] == "C"):
            num = num + 1*4**(len(pattern)-i-1)
        elif(pattern[i] == "G"):
            num = num + 2*4**(len(pattern)-i-1)
        elif(pattern[i] == "T"):
            num = num + 3*4**(len(pattern)-i-1)
    return(num)

def most_frequent_sort(text,k):
    index = [0]*(len(text)-k+1)
    count = [1]*(len(text)-k+1)
    words = []

    for i in range(len(text)-k+1):
        index[i] = pattern_to_number(text[i:i+k])
    sorted_index = sorted(index)

    #find the max run
    max_run = 0
    for i in range(1,len(sorted_index)):
        if(sorted_index[i-1] == sorted_index[i]):
            count[i] = count[i-1]+1

    for i in range(len(count)):
        if(max_run < count[i]):
            max_run = count[i]

    #add words that have max Run
    for i in range(len(count)):
        if(count[i] == max_run):
            words.append(number_to_pattern(sorted_index[i],k))
    
    return(words)
