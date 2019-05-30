#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 01:53:16 2018

@author: blakemcmurray
"""
def Suffix(Dna):
    word = Dna[1:]
    return(word)
def Prefix(Dna):
    word = Dna[0:len(Dna)-1]
    return(word)

def overlapGraph(Patterns):
    graph = {}  
    for i in range(len(Patterns)):
        for j in range(len(Patterns)):
            if Prefix(Patterns[i]) == Suffix(Patterns[j]):
                graph[Patterns[j]] = Patterns[i]
                
    return(graph)