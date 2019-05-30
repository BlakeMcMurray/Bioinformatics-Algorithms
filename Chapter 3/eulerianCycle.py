#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:41:13 2018

@author: blakemcmurray
"""
import random


gGraph = {"1":["2","6"],
                   "2":["3","8"],
                   "3":["4"],
                   "4":["2"],
                   "5":["7"],
                   "6":["9"],
                   "7":["8"],
                   "8":["1", "5"],
                   "9":["1"],}


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
    
findNumberOfEdges(gGraph)  

  
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


def findCircuit(Graph):
    node=random.randint(0,len(Graph)-1)
    currNode = str(node)
    stack=[]
    circuit=[]
    ct=0
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
        ct+=1
    circuit.reverse()
    circ=stack+[currNode]+circuit#    outcyc=stack.append(currNode).extend(circuit.reverse())
    return(circ)
              
def findEulerianCycle(Graph):
    node = str(random.randint(0,len(Graph)-1))
    node = str(1)
    return(findCircuit(Graph))