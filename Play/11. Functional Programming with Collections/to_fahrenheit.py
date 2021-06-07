# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:28:04 2018

@author: Asus
"""

def to_fahrenheit(t):
  result = list(map(lambda a: round(a * 1.8 + 32, 2), t))
  
  return result