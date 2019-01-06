# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:07:58 2018

@author: Asus
"""
    print("First case:")
    
    P= 1000
    n= 2
    r= 1
    
    print("\n" + "P = " + str(P) + ", n= " + str(n) + " and r = " + str(r) + "%")
     
    A = (P*((1+((float(r)/100)/float(n)))**(float(n)*2)))
    a = str(round(A,2))
    
    print("\n" + "The final amount at the end of the second year is: " + a) 
    
    print("\n" + "Second case:")
    
    P= 650
    n= 1
    r= -0.05
    
    print("\n" + "P = " + str(P) + ", n= " + str(n) + " and r = " + str(r) + "%")
     
    A = (P*((1+((float(r)/100)/float(n)))**(float(n)*2)))
    a = str(round(A,2))
    
    print("\n" + "The final amount at the end of the second year is: " + a) 
    
    print("\n" + "Third case:")
    
    P= input('Insert the "principal amount (the amount that the interest is provided on)": ')
    n= input('Insert the "the frequency that the interest is paid out (per year): ')
    r= input('Insert the "interest rate" (in percentage): ')
    
    print("\n" + "P = " + str(P) + ", n= " + str(n) + " and r = " + str(r) + "%") 
    
    A = (float(P)*((1+((float(r)/100)/float(n)))**(float(n)*2)))
    a = str(round(A,2))
    
    print("\n" + "The final amount at the end of the second year is: " + a) 
