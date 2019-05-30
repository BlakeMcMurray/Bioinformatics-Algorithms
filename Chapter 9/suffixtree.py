#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:48:07 2018

@author: blakemcmurray
"""

Patterns=['ATAGA$5','ATC$22','GAT$5']
def TrieConstruction(Patterns):
    Trie = {}
    Trie[0] = []
    counter = 1
    for i in Patterns:
        currentNode = Trie[0]
        for j in range(len(i)):
            if i[j-1]=='$':
                break
            if i[j]=='$':
                currentSymbol=i[j:]
            else:
                currentSymbol = i[j]
            boolean = False
            for k in currentNode:
                if currentSymbol in k:
                    boolean = True
                    currentNode = Trie[k[0]]
            if(boolean == False):
                currentNode.append([counter,currentSymbol])
                Trie[counter] = []
                newNode = Trie[counter]
                currentNode = newNode
                counter = counter + 1
    Trie2 = {}
    for i in Trie:
        if len(Trie[i]) != 0:
            Trie2[i] = Trie[i]
    del Trie
    Trie3={}
    for s in Trie2:
        buck=[]
        for t in range(len(Trie2[s])):
            buck.append([s,Trie2[s][t][0],Trie2[s][t][1]])
        Trie3[s]=buck
    return(Trie3)  
    
outrie=TrieConstruction(Patterns)

##################################################
Text='ATAAATG$'
def backtrack(node,sufftrie):
    ''' goes back in sufftrie to node predecessor '''
    if node==0:
        return(0)
    for s in sufftrie:
        for t in range(len(sufftrie[s])):
            if node==sufftrie[s][t][1]:
                return(sufftrie[s][t][0])
                
#def compress(node,outree):
    
    
           
def buildsufftree(Text):
    ''' builds suffix tree, by first building trie then
    compressing edges '''
    outree={}
    listt=[Text]
    for s in range(1,len(Text)):  # create list of suffixes
        listt.append(Text[len(Text)-s-1:]+str(len(Text)-s))
    listt=listt[1:]
    outree=TrieConstruction(listt)
    path=[] 
    for t in outree:  # creates list of paths that can be compressed
        for n in range(len(outree[t])):
            if outree[t][n][2][0] == '$':
#            
                path.append((n,outree[t][n][0]))
    spell=''
    s=0
    for s in range(len(path)):
        node=path[s][1] 
        indx=path[s][1] 
        spell=str(outree[node][0][2])
        notdone=1
        while(notdone):
            node1=backtrack(node,outree)
            if len(outree[node1])==1:
                spell=outree[node1][0][2]+spell
                node=node1
            else:
#
                for m in range(len(outree[node1])):
                    if node in outree[node1][m]:
                        notdone=0
                        outree[node1][m][2]+=spell
                        outree[node1][m][1]=indx
    outdict={}
    for n in outree:
        if (len(outree[n])==1 and '$' in outree[n][0][2]) or len(outree[n])>1:
            outdict[n]=outree[n]
    edg=[]
    for x in outdict:
        if len(outdict[x])==1 and not('$' in outdict[x][0][2]):
            edg.append(outdict[x][0][2])
        if len(outdict[x])>1:
            for u in range(len(outdict[x])):
                edg.append(outdict[x][u][2]) 
    for e in range(len(edg)):
        if '$' in edg[e]:
            edg[e]=edg[e][:edg[e].index('$')+1]
    del outree
    return(outdict,edg)

Text = "TTCATAGGACCCTAGAGAGCATCTTGCATGTGATTAAGTCACGGTCGCAGCTTGTGGTCTAAATCTCGTTCCGCTCTCTGAATTCCGGCATATATACACGGCCTTTACTCTTGGCAGAGCCAATTAAGTCCCTACGAGAGTGGCGCCTCAAGTTATCCTACAGACCAGATAGAACGGTTGCGGCCGCCTGACTATTATGAACTCCATAGAGTAGGTCTCGGCATTTAGCAGAGTAATAAAGACTGACCTAAGCCAACGAGATAGACGCCCGTGCTAGGCCGCCGTGATGTCGTGATAAGGGCGCAAAAGAACCCGTGGAATAGAAGTAGATTAGGCACACCACGAAAACCGTTTGTCAACACCACAGTGCCGCTGGCCTGAGTCACTAGACACCATAGCCGAGAACAACATCAGCGCAAATAACAGTGAGATCGCTTTACGGGCTTTGCTCAGATGTCAAGGGGTTTGGTTCCTTGAGCCAAGTATCGACGAAGCAAGCTTAGAAATATGACTATGTCGTCCCCATGTGATCGGTCTATATGTTACAATCTCCTTACATCGGGAGGTTTGATGCCTCCCTATAATTGTTCGCTGTTACTATGGCTTTTGTGGGTGATAACACGGTTGAGATCAACACACTTTGCCTTTGGCTCGTGATTGCTGCTGCAGCTAAAATTGACGGATTAACCAAGCGATACTTGGACCTAATAGTATCTGTAACGCCCAGGCAAGCAATTGAGAGAAGCAGGGCCGGACTCTACTCCAGACTAATTTGGTCTGCTAATACTTTAAGTTCGTCTCAAAGCAAGAACTACGGTTTGTAGGTGGAATATTTAAATCAAGGGAACGCGCC$"   
suftre,edg=buildsufftree(Text)   

for i in edg:
    print(i)