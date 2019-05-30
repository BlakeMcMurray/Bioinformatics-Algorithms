#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 01:23:27 2018

@author: blakemcmurray
"""

Dna = []

def reconstructPath(Dna):
    genome = ""
    for i in range(len(Dna)-1):
        genome = genome + Dna[i][0]
    genome = genome + Dna[len(Dna)-1]
    return(genome)