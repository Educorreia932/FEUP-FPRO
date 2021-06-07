# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:06:38 2018

@author: Asus
"""

def longest(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        lengths = {}
        
        for word in words:
            lengths[word] = len(word)

        return max(lengths, key = lengths.get)