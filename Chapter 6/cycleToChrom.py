#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:25:05 2018

@author: blakemcmurray
"""


def CyctoChromo(cycle):
    chromo=[]
    for s in range(int(len(cycle)/2)):
        if cycle[2*s]<cycle[2*s+1]:
            chromo.append(int(cycle[2*s+1]/2))
        else:
            chromo.append(-int(cycle[2*s]/2))
    return(chromo)

breakList = ""
with open(r'/Users/blakemcmurray/Downloads/rosalind_ba6g.txt') as f:
    breakList = f.read().replace('(','').replace(')','').replace(' ',', ')

cycle = [1, 2, 4, 3, 5, 6, 8, 7, 9, 10, 12, 11, 14, 13, 15, 16, 18, 17, 20, 19, 22, 21, 23, 24, 25, 26, 27, 28, 30, 29, 31, 32, 34, 33, 36, 35, 37, 38, 39, 40, 42, 41, 43, 44, 46, 45, 48, 47, 50, 49, 51, 52, 53, 54, 55, 56, 57, 58, 60, 59, 62, 61, 64, 63, 65, 66, 68, 67, 70, 69, 71, 72, 73, 74, 75, 76, 78, 77, 80, 79, 82, 81, 84, 83, 86, 85, 87, 88, 90, 89, 91, 92, 94, 93, 95, 96, 97, 98, 99, 100, 102, 101, 103, 104, 106, 105, 107, 108, 109, 110, 112, 111, 114, 113, 116, 115, 118, 117, 119, 120, 121, 122, 124, 123, 126, 125, 128, 127, 130, 129, 132, 131]
chrome = CyctoChromo(cycle)
string1 = ""
for i in chrome:
    print(str(i) + " ", end='')