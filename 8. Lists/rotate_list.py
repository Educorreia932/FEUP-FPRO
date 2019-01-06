# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 22:19:15 2018

@author: Asus
"""

def rotate_list(l):
    counter = 0
    n = 0
    
    while n < 3:
        last = l[-1]
        for element in l:
            if counter == len(l) - 1:
                l[-2] = last
                
            else:                    
                l[counter - 1] = element
                counter += 1
            
        counter = 0
        n += 1

    return l   