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
    no_dup = []
    for k in range (len(list)):
        if list[k] not in no_dup:
            no_dup.append(list[k])
    return(no_dup)   
    
def comp_of_s(k, Text):
    list = []
    for i in range(len(Text)-k+1):
        list.append(Text[i:i+k])
    return(list) 
  
def debruijn_construction(k, Text):
    edges = comp_of_s(k, Text)
    graph = {}
    for i in range(len(edges)):
        prefix = prefix(edges[i])
        suffix = suffix(edges[i])
        if prefix not in graph:
            graph[prefix] = []
            graph[prefix].append(suffix)
        elif prefix in graph:
            graph[prefix].append(suffix) 
    for i in graph:
        graph[i] = elim_dup(graph[i])
        
    return(graph)

