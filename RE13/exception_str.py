# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:40:12 2019

@author: Asus
"""

def exception_str(f):
    try:
        f()
    
    except Exception as ex:
        return(str(ex))
        
    else:
        return("No exception was raised")