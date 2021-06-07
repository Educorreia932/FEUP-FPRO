# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:31:54 2019

@author: Asus
"""

from statistics import median 

def batch_norm(alist, batch_size):
    sublists = []
    sublist = []
    
    sublists = [alist[batch_size*i:batch_size*(i+1)] for i in range(int(len(alist)/batch_size + 1))]
    
    def chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i: i + n]
        
    sublists = list(chunks(alist, batch_size))   
        
    for sublist in sublists:
        new_list = []
        sublist_copy = sublist.copy()
        med = median(sublist)
        new_list = list(map(lambda a: a - med, sublist_copy))
            
        yield new_list

print(list(batch_norm([-1, 0, 1, 1, 2, 4], 3)))  
