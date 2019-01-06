# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:15:43 2018

@author: Asus
"""

def rm_letter_rev(l, astr):
  result = astr.replace(l, "")[::-1]
  return result

print(rm_letter_rev("s", "A Style Guide is about consistency"))

    
      