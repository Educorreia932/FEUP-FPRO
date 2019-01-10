# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:56:27 2019

@author: Asus
"""

def compatible(A, B):
    if len(A[0]) != len(B):
        return AssertionError("A and B cannot be multiplied")
    
    else:
        return "A and B can be multiplied"