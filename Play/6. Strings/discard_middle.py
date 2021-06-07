# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:38:12 2018

@author: Asus
"""

def discard_middle(s):
  if len(s) <= 3:
    return ""
  else:
    return s[0:2] + s[-2] + s[-1]
  
print(discard_middle("fohtrehyfi"))