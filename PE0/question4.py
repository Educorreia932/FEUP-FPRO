# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:09:44 2018

@author: Asus
"""

LE = int(input("Insert your LE classification: "))
RE = int(input("Insert your RE classification: "))
PE = int(input("Insert your PE classification: "))
TE = int(input("Insert your TE classification: "))

grade = (LE + RE + 4 * PE + 4 * TE) / 50

if LE < 0 or LE > 100 or LE < 0 or RE > 100 or RE < 0 or PE > 100 or PE < 0 or TE > 100 or TE < 0:
  print("Input error")
  
elif PE < 40 or TE < 40:
  print("RFC")

else: 
  print(round(grade, 0))  