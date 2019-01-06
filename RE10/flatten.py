# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:35:08 2018

@author: Asus
"""

def flatten(alist):  
  if alist == []:
    return alist
  
  elif type(alist[0]) == list:
    return flatten(alist[0]) + flatten(alist[1:])
  
  else:
    return alist[:1] + flatten(alist[1: ])