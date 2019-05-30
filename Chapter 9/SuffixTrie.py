#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:32:08 2018

@author: blakemcmurray
"""
Text = "ATAAATG$"

def SuffixTrieConstruction(Text):
    Patterns = []
    for i in range(len(Text)):
        Patterns.append(Text[i:])
    
    print(Patterns)
        
    Trie = {}
    Trie[0] = ([])
    counter = 1
    for i in range(len(Patterns)):
        currentNode = Trie[0]
        for j in range(len(Patterns[i])):
            currentSymbol = Patterns[i][j]
            boolean = False
            for k in currentNode:
                if currentSymbol in k:
                    boolean = True
                    currentNode = Trie[k[0]]
            if(boolean == False):
                if(currentSymbol == "$"):
                    currentNode.append((i,currentSymbol))
                    counter = counter+1
                else:
                    currentNode.append((counter,currentSymbol))
                    Trie[counter] = []
                    newNode = Trie[counter]
                    currentNode = newNode
                    counter = counter + 1
    Trie2 = {}
    for i in Trie:
        if len(Trie[i]) != 0:
            Trie2[i] = Trie[i]
            
    deleteTrie = Trie2
    strings = []
    currentNode = Trie2[0]
    while(len(deleteTrie) != 0):
        
        

print(SuffixTrieConstruction(Text))    
#def SuffixTrieConstruction(Text):
    
