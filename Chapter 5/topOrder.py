#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:00:03 2018

@author: blakemcmurray
"""
import copy


def depthfsearch(Vis,currnode,visitedN,Graph):
    Vis[currnode]=1
    for edge in Graph[currnode]:
        if Vis[edge]==0:
            depthfsearch(Vis,edge,visitedN,Graph) 
    visitedN.append(currnode)
    return(visitedN)

def GraphCreator(Graph):
    nodes = []
    newDict = copy.deepcopy(Graph)
    for i in Graph:
        nodes.append(i)
    for i in list(Graph):
        for j in range(len(Graph[i])):
            if Graph[i][j] not in nodes:
                newDict[Graph[i][j]] = []
    return(newDict)


def topo_sort(Graph):
    Graph=GraphCreator(Graph)
    Vis = {}
    toporder = {}
    order = []
    for t in range(len(Graph)):
        toporder[t] = -1
    for s in Graph:
        Vis[s] = 0
        for t in range(len(Graph[s])):
            Vis[Graph[s][t]] = 0 
    N = len(Graph)
    setG = set(Graph)
    m = N-1
    while(len(setG)>0):
        try:
            s = setG.pop()
            if Vis[s] == 0:
                visitedN = []
                depthfsearch(Vis,s,visitedN,Graph)
                setG = setG.difference(set(visitedN))
                for t in range(len(visitedN)):
                    toporder[m-t] = visitedN[t]
                m = m-len(visitedN) 
#                print(visitedN,s,toporder,m,setG)
        except KeyError:
            break 
    for s in range(len(toporder)):
        order.append(toporder[s])    
    return(order)
graph = {1: [2],
         2: [3],
         4: [2],
         5: [3]}
    
filen='/Users/blakemcmurray/text.txt'
fileo='/Users/blakemcmurray/output.txt'

def readin(filen):
    with open(filen) as f:
        read_data = f.read() 
    return(read_data)

def writeout(fileo,strng):
    with open(fileo,'w') as f:
        f.write(strng)
    return()
        
outpp=readin(filen) #####  copy an paste a head of time the input data for graph into filen
outp1=outpp.replace(' -> ','":["')
outp2=outp1.replace('\n','"];"')
outp3=outp2.replace(',','","')
outp4=outp3.replace(';',',')
outp5='{"'+outp4+'"]}'
writeout(fileo,outp5) 

graph ={"0":["2","32"],"1":["12","22"],"10":["13","21"],"11":["23","33"],"12":["14","18","19","20","27","32","33"],"13":["18","24"],"14":["15","16","17","23"],"15":["18","24"],"16":["22"],"18":["19","27","33"],"2":["26","30","31","7"],"20":["27","28"],"21":["23","26"],"22":["26"],"23":["29"],"24":["25","26"],"26":["29"],"27":["32"],"29":["32"],"3":["13","25","6","8"],"4":["8"],"5":["14","16","18","19","22","24","7"],"6":["18","30","31","32","33"],"7":["16","24"],"8":["11","13","17","25"],"9":["11","18"]}
sort = topo_sort(graph)
for i in sort:
    print(i + ", ", end = ''),