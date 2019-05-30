#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:00:03 2018

@author: blakemcmurray
"""
import copy


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

def GraphCreatorfull(Graph):
    nodes = []
    newDict = copy.deepcopy(Graph)
    for i in Graph:
        nodes.append(i)
    for i in list(Graph):
        for j in range(len(Graph[i])):
            if Graph[i][j][0] not in nodes:
                newDict[Graph[i][j][0]] = []
    return(newDict)

def makeGraph(inplist):
    Graph={}
    pGraph={}
    for s in range(0,len(inplist)-3,3):
        if not(inplist[s] in Graph):
            Graph[inplist[s]]=[]
            pGraph[inplist[s]]=[]
    for s in range(0,len(inplist)-3,3):
        Graph[inplist[s]].append((inplist[s+1],int(inplist[s+2])))
        pGraph[inplist[s]].append(inplist[s+1])
    return(Graph,pGraph)

def Predecessor(Graph):
    Pred=GraphCreatorfull(Graph)
    for s in Pred:
        Pred[s]=[]
    for s in Pred:
        for t in Graph:
            if s in Graph[t]:
                Pred[s].append(t)
    return(Pred)

def maxPathDAG(start,end,inlist):
    camefrom = ''
    CGraph = {}
    TGraph,pGraph = makeGraph(inlist)
    TGraph = GraphCreatorfull(TGraph)
    CGraph = GraphCreator(pGraph)
    PGraph = GraphCreator(pGraph)
    Pred=Predecessor(PGraph)
    topsortind=topo_sort(PGraph)
    for s in PGraph:
        CGraph[s]=(-float('inf'),'-1')
    CGraph[str(start)]=(0,'-1')
    for ind in topsortind:
        maxx=CGraph[ind][0]
        for pred in Pred[ind]:
            for r in range(len(TGraph[str(pred)])):
                if TGraph[str(pred)][r][0]==ind:
                    predind=r
            if maxx < TGraph[str(pred)][predind][1]+CGraph[str(pred)][0]:
                maxx=TGraph[str(pred)][predind][1]+CGraph[str(pred)][0]
                camefrom=str(pred)
            CGraph[ind]=(maxx,camefrom)
    return(CGraph)

def Backtrack(outgraph,start,end):
    send=end
    path=[]
    while(not(start==end)):
        path.append(outgraph[end][1])
        end=outgraph[end][1]
    path.reverse()
    path.append(send)
    return(path)
    
def readin(filen):
    with open(filen) as f:
        read_data = f.read() 
    return(read_data)   

filen = '/Users/blakemcmurray/Downloads/rosalind_ba5d.txt'
inpp = readin(filen)
inpp1 = inpp.replace('\n','","')
inpp4 = inpp1.replace(':','","')
inpp2 = inpp4.replace('->','","')
inlist = ["21","31","11","9","26","12","19","24","12","24","30","1","16","32","20","14","28","14","11","13","1","19","22","8","8","32","18","33","36","38","14","20","27","15","31","12","8","37","29","10","14","6","4","21","32","14","39","12","34","35","37","20","28","21","12","13","6","10","19","37","12","16","3","34","37","2","8","18","6","0","17","4","21","28","28","0","15","32","38","39","16","35","39","18","8","17","35","17","27","10","20","37","31","25","35","5","2","30","5","7","25","2","2","18","30","14","38","32","24","35","39","2","15","30","8","9","9","36","37","38","16","25","22","16","26","28","16","27","28","14","35","28","24","39","19","19","32","25","18","25","5","35","36","34","35","37","4","7","26","22","6","15","12","16","29","10","6","31","28","10","27","38","5","23","11","20","33","21","3","6","16","20","36","29","3","23","18","1","19","3","14","25","13","5","14","32","28","38","22","0","23","4","15","18","32","21","26","19","31","36","19","3","18","9","6","37","37","2","25","8","7","12","29","13","14","26","3","39","27","29","37","29"]

start = str(0)
end = str(23)  
cGraph = maxPathDAG(start,end,inlist)       # cGraph is the C dict. look for index=maxCost
print(cGraph)

print(Backtrack(cGraph,start,end))