#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:20:22 2018

@author: exame
"""

def exactly(s):
    counter = 0
    interrogation = 0
    index = 0
    result = ()
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers_list = []
    
    for character in s:
        if character in numbers:
            numbers_list.append((character, counter))
        counter += 1
    
    for number in numbers_list:
        
        low = number[1]     
        lower = number[0]
        
        if index + 1 > len(numbers_list) - 1:
            break
        
        high = numbers_list[index + 1][1]
        higher = numbers_list[index + 1][0]
        
        interval = s[low: high]
        
        if (int(lower) + int(higher)) == 10:
            for char in interval:
                if char == "?":
                    interrogation += 1

            if interrogation != 3: 
                result = (lower + higher,) 
                return "The sequence " + s + " is NOT OK with first violation with pair: " + str(result)
            
            else:
                result += (lower + higher,)
        
        interrogation = 0        
        index += 1        
                
    return "The sequence " + s + " is OK with the pairs: " + str(result)                

print(exactly("htrtr24?h56h56??29004??34"))    