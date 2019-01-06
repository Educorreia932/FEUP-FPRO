# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 08:51:34 2018

@author: Asus
"""

n = int(input("Insira a quantidade de números que pretende inserir: "))
result = ""

for number in range (n+1):
    if number % 3 == 0 and number % 5 != 0:
      number = "Fizz "
    elif number % 3 != 0 and number % 5 == 0:
      number = "Buzz "
    elif number % 3 == 0 and number % 5 == 0 :
      number = ""
    else:
      number = str(number) + " " 
    result = result + str(number)

print(result)
      
    