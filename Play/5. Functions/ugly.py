# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:56:14 2018

@author: Asus
"""

def ugly(n):
  def is_prime(number):
    for i in range(2, number):
      if number % i == 0:
        return False
      else:
        return True
  
  primes = [2, 3, 5]
  
  if n == 1:
    return True
  
  for u in range(2, n):
    if is_prime(u) == True and u not in primes and n % u == 0:
      return False
    
  for j in primes:
    if n % j == 0:
      return True
    
  if is_prime(n) == True and n not in primes:
    return False   
        
