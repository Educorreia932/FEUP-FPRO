# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:48:02 2018

@author: Asus
"""

def nth_lowest(lnum, n):
  lnum = sorted(lnum)
  result = lnum[n - 1]
  
  return result
