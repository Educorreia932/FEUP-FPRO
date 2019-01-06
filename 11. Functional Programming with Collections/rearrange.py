# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:15:35 2018

@author: Asus
"""

def rearrange(l):
  positive = list(filter(lambda a: a > 0, l))
  negative = list(filter(lambda a: a <= 0, l))
  result = negative + positive
  
  return result