#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 01:53:16 2018

@author: blakemcmurray
"""
def suffix(dna):
    word = dna[1:]
    return(word)

def prefix(dna):
    word = dna[0:len(dna)-1]
    return(word)

def overlap_graph(patterns):
    graph = {}  
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if prefix(patterns[i]) == suffix(patterns[j]):
                graph[patterns[j]] = patterns[i]
                
    return(graph)
