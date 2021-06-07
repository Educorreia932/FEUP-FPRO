# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:11:19 2019

@author: Asus
"""

def sum_pairs(alist):
    result = []
    index = 0
    
    for element in alist:
        try:
            1 + element

        except TypeError:
            index += 1        
        
        else:
            if index < len(alist) - 1 and type(alist[index + 1]) == int:
               pair = element + alist[index + 1]
               result.append(pair)
                      
            elif index == len(alist) - 1:
                break       
        
            index += 1
        
    return result

print(sum_pairs([10, 3, 5, 'NA', 9, 1]))