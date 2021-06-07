# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:15:01 2018

@author: Asus
"""

def longest(s):
  def sort_key(s):
    return len(s)
  
  s = sorted(s.split(), key = sort_key, reverse = True)
  
  return len(s[0])  