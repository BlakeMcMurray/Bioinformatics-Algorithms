#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:31:07 2018

@author: blakemcmurray
"""
def Suffix(Dna):
    word = Dna[1:]
    return(word)
    
def Prefix(Dna):
    word = Dna[0:len(Dna)-1]
    return(word)
    
def elimDup(list):
    noDup = []
    for k in range (len(list)):
        if list[k] not in noDup:
            noDup.append(list[k])
    return(noDup)   
    
def compOfString(k, Text):
    list = []
    for i in range(len(Text)-k+1):
        list.append(Text[i:i+k])
    return(list) 
  
def deBruijnConstruction(k, Text):
    edges = compOfString(k, Text)
    deBruijnGraph = {}
    for i in range(len(edges)):
        prefix = Prefix(edges[i])
        suffix = Suffix(edges[i])
        if prefix not in deBruijnGraph:
            deBruijnGraph[prefix] = []
            deBruijnGraph[prefix].append(suffix)
        elif prefix in deBruijnGraph:
            deBruijnGraph[prefix].append(suffix) 
    for i in deBruijnGraph:
        deBruijnGraph[i] = elimDup(deBruijnGraph[i])
        
    return(deBruijnGraph)