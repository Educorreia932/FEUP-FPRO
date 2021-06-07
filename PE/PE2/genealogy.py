#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:20:49 2018

@author: exame
"""

def genealogy(l):
    def rule(person):
        if person[1] == "sibling":
            result = 1
        elif person[1] == "parent":
            result = 2    
        elif person[1] == "cousin":
            result = 3        
        elif person[1] == "grandparent":
            result = 4
            
        return (result, person[0])

    l = sorted(l, key = rule)
    
    return l