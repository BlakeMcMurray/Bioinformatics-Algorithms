#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:37:04 2018

@author: blakemcmurray
"""
Down = [[1,4,4,5],[0,6,4,6],[2,5,5,8],[4,2,2,5],[3,1,1,3]]
Right = [[3,2,4,0],[3,2,4,2],[0,7,3,3],[3,3,0,2],[1,3,2,2]]

Down = []
Right = []
with open(r'/Users/blakemcmurray/Downloads/rosalind_ba5b (2).txt') as f:
    boolean = False
    for line in f: 
        l = line.strip()
        l = l.replace(" ","")

        if "-" not in line and len(l) == 7:
            if boolean == False:    
                count = 0
                for i in (l):
                    Down.append([])
                    Down[count].append(int(i))
                    count = count +1
                boolean = True
            else:
                count = 0
                for i in l:
                    Down[count].append(int(i))
                    count = count + 1

        if ("-" not in line and len(l) < 7):
            count = len(Right)
            Right.append([])
            for i in l:
                Right[count].append(int(i))
            count = count + 1
            
                  
f.close()



def ManhattanTourist(n,m,Down,Right):
    s = {}
    s[0,0] = 0    
    for i in range(1,n+1):
        s[i,0] = s[i-1,0] + Down[0][i-1]

    for j in range(1,m+1):
        s[0,j] = s[0,j-1] + Right[0][j-1]
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i,j] = max(s[i,j-1] + Right[i][j-1],s[i-1,j]+Down[j][i-1])
    return s[n,m]

graph = ManhattanTourist(12,6,Down,Right)
print(graph)