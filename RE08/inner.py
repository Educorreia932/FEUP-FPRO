# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:50:51 2018

@author: Asus
"""

def inner(u, v):
  result = 0
  
  for i in range(len(u)):
    result += u[i] * v[i]
      
  return result

