# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:08:14 2018

@author: Asus
"""
result = ""

side_1 = float(input("Insira o comprimento do 1º lado: "))
side_2 = float(input("Insira o comprimento do 2º lado: "))
side_3 = float(input("Insira o comprimento do 3º lado: "))

if (side_1 + side_2) > side_3 and (side_1 + side_3) > side_2 and (side_2 + side_3) > side_1:
  if side_1 == side_2 == side_3:
    result = "Equilateral"
  elif side_1 != side_2 != side_3:
    result = "Scalene"
  else:
    result = "Isosceles"
else:
  result = "Not a triangle"

print(result)
