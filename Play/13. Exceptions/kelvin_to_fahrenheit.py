# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:53:18 2019

@author: Asus
"""

def kelvin_to_fahrenheit(temp):
    try:
        assert temp >= 0 
    
    except AssertionError:
        return AssertionError("Colder than absolute zero!")
    
    else:        
        result = int((temp * 1.8) - 459.67)

        return result

print(kelvin_to_fahrenheit(273))