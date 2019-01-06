# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:30:39 2018

@author: Asus
"""

from functools import reduce

def map_filter_reduce(lst, f1, f2, f3):
  result = int(reduce(f3, (map(f2, filter(f1, lst)))))
  
  return result