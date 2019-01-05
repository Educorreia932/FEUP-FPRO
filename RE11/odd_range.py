# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:44:41 2018

@author: Asus
"""

def odd_range(start, stop, step):
  if start % 2 == 0:
    start += 1

  while start < stop:
    yield start
    start += step * 2