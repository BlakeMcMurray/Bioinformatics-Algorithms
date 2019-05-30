#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:18:22 2018

@author: blakemcmurray
"""
import math
def DPChange(money, coins):
    minNumCoins = {}
    minNumCoins[0] = 0
    for m in range(1, money+1):
        minNumCoins[m] = math.inf
        for i in range(len(coins)):
            if m >= coins[i]:
                if minNumCoins[m - coins[i]]+1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m - coins[i]] +1
    return minNumCoins[money]


coins = [1,3,5,15,19,22]
print(DPChange(19926,coins))