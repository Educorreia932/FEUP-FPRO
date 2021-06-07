# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 16:07:25 2019

@author: Asus
"""

from math import log

def tfidf(documents):
    words = []
    frequency = {}
    result = {}
    
    for document in documents:
        for word in document.split():
            words.append(word.lower())
            
    words = list(dict.fromkeys(words))
            
    for word in words:
        count = []        
        
        for document in documents:
            document = document.lower()
            count.append(document.split().count(word))
            
        frequency[word] = count  
    
    for key in frequency:
        value = []
        N = len(documents)
        n = 0
        
        for count in frequency[key]:
            if count != 0:
                n += 1
        
        idf = log(N / n)
        
        for element in  frequency[key]:
            value.append(round((element * idf), 3))
        
        result[key] = value
        
    return result