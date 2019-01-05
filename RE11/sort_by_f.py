# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:14:18 2018

@author: Asus
"""

def sort_by_f(l):
  return sorted(l, key = lambda a: 5 - a if a >= 5 else a)