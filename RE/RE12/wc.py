# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def wc(filename):
    result = []
    
    with open(filename, "r") as file:
        lines = file.readlines()
        result.append(len(lines))
        
        words = 0

        for line in lines:
            words += len(line.split())
        
        result.append(words)
        
        characters = 0
        
        for line in lines:
            for character in line:
                characters += 1
            
        result.append(characters)
        
    return tuple(result)