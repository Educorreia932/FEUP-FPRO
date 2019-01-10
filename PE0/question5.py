# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:41:53 2018

@author: Asus
"""

lower = int(input("Insert the lowest number: "))
upper = int(input("Inser the higher number: "))

result = ""

for i in range(lower, upper + 1):
  if i < 0:
    pass
  elif i > 1:
    counter = 0
    for n in range(1, i + 1):
      if i % n == 0:
        counter += 1
    if counter <= 2:
      result += str(i) + " "
  
print("Prime numbers between " + str(lower) + " and " + str(upper) + " are: \n" + result)
