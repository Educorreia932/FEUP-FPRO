# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:50:46 2019

@author: Asus
"""

def paint(n, boards):
    if n == 1:
        return max(boards)
    
    else:
        times = []
        
        for i in range(1, len(boards) - n + 1):
            times.append(paint(1, boards[:i] + paint(n - 1, boards[i: ])))
        
        return min(times)