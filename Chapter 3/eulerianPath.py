#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:50:26 2018

@author: blakemcmurray
"""
import random

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
    
def GraphCreator(Graph):
    nodes = []
    newDict = Graph
    for i in Graph:
        nodes.append(i)
    for i in list(Graph):
        for j in range(len(Graph[i])):
            if Graph[i][j] not in nodes:
                newDict[Graph[i][j]] = []
    return(newDict)

def Out(Graph, node):
    return(len(Graph[node]))
    

def In(Graph, node):
    count = 0
    for i in Graph:
        for k in range(len(Graph[i])):
            if node == Graph[i][k]:
                count = count+1
    return(count)
    
def findStartNode(Graph):
    for i in Graph:
        count = In(Graph, i) - Out(Graph, i)
        if count == -1:
            return i
        
print(findStartNode(gGraph))

def findEndNode(Graph):
    for i in Graph:
        count = In(Graph, i) - Out(Graph, i)
        if count == 1:
            return i

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


def findPath(Graph):
    sNode = findStartNode(Graph)
    currNode = str(sNode)
    stack=[]
    circuit=[]
    circ=[]
    stack.append(currNode)
    while(stack):
        if not(hasNoNeighbors(Graph, currNode)):
            stack.append(currNode)
            edge = None
            edge = random.choice(Graph[currNode])
            Graph = deleteNeighbor(Graph, currNode, edge)
            currNode = edge
        elif hasNoNeighbors(Graph,currNode):
            circuit.append(currNode)
            currNode = stack.pop()
        elif findNumberOfEdges(Graph)==1:
            break
    circuit.reverse()
    circ=stack+[currNode]+circuit
    return(circ[1:])
              
def findEulerianPath(Graph):
    RealGraph = GraphCreator(Graph)
    return(findPath(RealGraph))