#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:15:55 2018

@author: blakemcmurray
"""
chrome = (+1, -2,-3,4)
def chrome_to_cycle(chrome):
    s = []
    for i in range(len(chrome)):
        j = chrome[i]
        if(j < 0):
            s.append(2*(-j))
            s.append(2*(-j)-1)
        if(j > 0):
            s.append(2*(j)-1)
            s.append(2*(j))
    return(s)

    
chrome = (+1, +2, +3, -4, -5, +6, +7, -8, +9, +10, -11, -12, +13, +14, -15, +16, -17, -18, +19, -20, +21, +22, +23, +24, +25, -26, +27, +28, -29, -30, -31, -32, -33, -34, +35, -36, +37, +38, +39, +40, -41, +42, -43, -44, -45, -46, +47, -48, -49, +50, +51, +52, +53, +54, -55, -56, -57, +58, +59, -60, +61, -62, -63, +64, -65, -66)
cycle = chrome_to_cycle(chrome)

string1 = ""
for i in cycle:
    print(str(i) + " ", end='')
