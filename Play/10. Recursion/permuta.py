# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:04:32 2019

@author: Asus
"""

global result
result = [] 

global final_result
final_result = []

def permutations(alist):
    if len(alist) == 1:        
        result.append(alist[0]) 
        global final_result
        final_result += result          
        result.pop()
        
    for i in range(0, len(alist)):
        result.append(alist[i])
        permutations(alist[:i] + alist[i+1:])
        result.pop()  
        
    return final_result

def permuta(alist, step = 0):
    alist = permutations(alist)
    result = []
    index = 0
 
    while True:
        if index <= len(alist) - 3:
            result.append([alist[index], alist[index + 1], alist[index + 2]])   
            
        else:
            break
        
        index += 3
        
    return result  