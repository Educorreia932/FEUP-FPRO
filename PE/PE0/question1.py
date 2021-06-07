# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:20:26 2018

@author: Asus
"""

P = 1000

t = 1

print("First case")

r1 = float(input("Insert the interest rate: "))
n1 = float(input("Insert the the frequency that the interest is paid out (per year): "))

A1= float(P)*(1+r1/n1)**(n1*float(t))

print("Second case")

r2 = float(input("Insert the interest rate: "))
n2 = float(input("Insert the the frequency that the interest is paid out (per year): "))

A2= float(P)*(1+r2/n2)**(n2*float(t))

print("For r= " + str(r1) + "and n=" + str(n1) + "you'll have " + str(A1))
print("For r= " + str(r2) + "and n=" + str(n2) + "you'll have " + str(A2))