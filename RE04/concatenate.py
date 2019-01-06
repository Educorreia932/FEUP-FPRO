# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:08:14 2018

@author: Asus
"""
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo numero: "))
    
count = 0
    
while(n2 >= 1):
  n2 = n2 / 10
  count = count + 1
      
n1 = n1 * (10 ** count)
n2 = n2 * (10 ** count)
    
result = n1 + n2
    
print(int(result))
