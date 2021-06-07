# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:24:20 2018

@author: Asus
"""

def to_celsius(t):
  result = list(map(lambda a: round((a - 32) / 1.8, 1), t))
  
  return result