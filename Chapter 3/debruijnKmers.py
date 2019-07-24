#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:31:07 2018

@author: blakemcmurray
"""
def suffix(Dna):
    word = Dna[1:]
    return(word)
    
def prefix(Dna):
    word = Dna[0:len(Dna)-1]
    return(word)
    
def elim_dup(list):
    noDup = []
    for k in range (len(list)):
        if list[k] not in noDup:
            noDup.append(list[k])
    return(noDup)   
    
def comp_of_s(k, Text):
    list = []
    for i in range(len(Text)-k+1):
        list.append(Text[i:i+k])
    return(list) 
  
patterns = []
with open(r'/Users/blakemcmurray/Downloads/rosalind_ba3e.txt') as f:
 
    for line in f:   
        l = line.strip()
        patterns.append(l)
        
f.close()

def debruijn_kmers(patterns):
    edges = patterns
    graph = {}
    for i in range(len(edges)):
        prefix = prefix(edges[i])
        suffix = suffix(edges[i])
        if prefix not in graph:
            graph[prefix] = []
            graph[prefix].append(suffix)
        elif prefix in graph:
            graph[prefix].append(suffix) 
        
    return(graph)
