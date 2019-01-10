# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:45:43 2018

@author: Asus
"""

num = float(input("Insert a number: "))

x0 = num/2
x1= (x0 + num / x0) / 2

while round(x0, 2) != round(x1, 2):
  x0 = x1
  x1 = (x0 + num / x0) / 2

result = (round(x1,3))

print (format(result, ".3f"))