# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:34:54 2018

@author: Asus
"""

def rec_to_base(n, base):
  correspondent = "0123456789ABCDEF"
  
  if n < base:
    return correspondent[n]

  return (rec_to_base(n // base, base) + correspondent[n % base])
