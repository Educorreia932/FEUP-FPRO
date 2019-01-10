#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:27:25 2018

@author: exame
"""

def caesar(message):
    result = ""
    counter = 0
    
    def fibonacci(n):
        f = (((1 + 5 ** (1 / 2)) ** n) - ((1 - 5 ** (1 / 2)) ** n)) / ((2 ** n) * (5 ** (1/2)))
        
        return int(f)
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for letter in message:
        shift = fibonacci(counter)
        
        if letter not in alphabet:
            result += letter
            
        else:        
            letter_index = alphabet.index(letter)

            final_index = letter_index - shift
            
            while final_index < 0:
                final_index = final_index + 26
                
            result += alphabet[final_index]
                      
        counter += 1
    
    return result

