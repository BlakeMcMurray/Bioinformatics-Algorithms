#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:18:34 2018

@author: blakemcmurray
"""
import random
def findHammingDist(DNA1, DNA2):
    dist = 0
    for i in range(len(DNA1)):
        if DNA1[i] != DNA2[i]:
            dist += 1    
    return(dist)

def elimDup(list):
    noDup = []
    for k in range (len(list)):
        if list[k] not in noDup:
            noDup.append(list[k])
    return(noDup)

def dNeighbor(Text,d):
    if d==0:
        return([Text])
    if len(Text)==1:
        return(["0","1"])
    neighb=[]
    SuffixNeighbors=dNeighbor(Text[1:],d)
    for s in SuffixNeighbors:
        if findHammingDist(s,Text[1:])<d:
            for e in "01":
                neighb.append(e+s)
        else:
            neighb.append(Text[0]+s)
    return (neighb)

def Suffix(Dna):
    word = Dna[1:]
    return(word)
    
def Prefix(Dna):
    word = Dna[0:len(Dna)-1]
    return(word) 

def deBruijnKmer(Patterns):
    edges = Patterns
    deBruijnGraph = {}
    for i in range(len(edges)):
        prefix = Prefix(edges[i])
        suffix = Suffix(edges[i])
        if prefix not in deBruijnGraph:
            deBruijnGraph[prefix] = []
            deBruijnGraph[prefix].append(suffix)
        elif prefix in deBruijnGraph:
            deBruijnGraph[prefix].append(suffix) 
        
    return(deBruijnGraph)


def hasNoNeighbors(Graph, node):
    if(len(Graph[node]) == 0):
        return True
    else:
        return False

def findNumberOfEdges(Graph):
    count = 0
    for i in Graph:
        count = count + len(Graph[i])
    return(count)
      
def deleteNeighbor(Graph, node, neighbor):
    index = 0
    toReturn = []
    for i in range(len(Graph[node])):
        if Graph[node][i] == neighbor:
            index = i
    for i in range(len(Graph[node])):
        if i != index:
            toReturn.append(Graph[node][i])
    Graph[node] = toReturn
    return Graph


def findCircuit(Graph,k):
    node='0'*(k-1)
    currNode = str(node)
    stack=[]
    circuit=[]
    circ=[]
    while(findNumberOfEdges(Graph)>0):
        if not(hasNoNeighbors(Graph, currNode)):
            stack.append(currNode)
            edge = random.choice(Graph[currNode])
            Graph = deleteNeighbor(Graph, currNode, edge)
            currNode = edge
        elif hasNoNeighbors(Graph,currNode):
            circuit.append(currNode)
            currNode = stack[-1]
            stack=stack[:-1]
        elif findNumberOfEdges(Graph)==1:
            break
    circuit.reverse()
    circ=stack+[currNode]+circuit
    
    #    outcyc=stack.append(currNode).extend(circuit.reverse())
    return(circ)
              
def findEulerianCycle(Graph,k):
    return(findCircuit(Graph,k))

def KUniversalString(k):
    text = "0"*k
    patterns = dNeighbor(text, 999)
    graph = deBruijnKmer(patterns)
    cycle = findEulerianCycle(graph,k)
    string = ""
    boolean = False
    for ind in range(0, len(cycle)-(k-1)):
        i = cycle[ind]
        if boolean == False:
            string = string + i
            boolean = True
        else:
            string = string + i[k - 2]
    return(string)

print(KUniversalString(8))