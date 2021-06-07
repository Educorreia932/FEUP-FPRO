# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:20:06 2018

@author: Asus
"""

def minion(astring):
    Kevin = {}
    Stuart = {}
    vowels = ["A", "E", "I", "O", "U"]
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    order = []
    index = 0
    result = ""
    
    for character in astring:
        if character in vowels:
            char_index = index + 1
            
            for letter in astring[index: ]:
                if astring[index: char_index] not in Kevin:
                    Kevin[astring[index: char_index]] = 1
                    
                else:
                    Kevin[astring[index: char_index]] += 1
                    
                char_index += 1
                    
        index += 1        
        
    index = 0    

    for character in astring:
        if character in consonants:
            char_index = index + 1
            
            for letter in astring[index: ]:
                if astring[index: char_index] not in Stuart:
                    Stuart[astring[index: char_index]] = 1
                    
                else:
                    Stuart[astring[index: char_index]] += 1
                    
                char_index += 1
                    
        index += 1  
          
    kevin_points = sum(Kevin.values())
    stuart_points = sum(Stuart.values())
    
    if kevin_points == stuart_points:
        return "It was a draw!"
    
    else:
        if kevin_points > stuart_points:
            winner = "Kevin"
            points = kevin_points
            
        else: 
            winner = "Stuart"
            points = stuart_points
        
        result += "The winner was " + winner + " with a total of " + str(points) + " points: \n"
        
        sort = sorted(eval(winner).keys(), key = lambda a: len(a))
    
        for element in sort:
            order.append((element, eval(winner)[element]))
        
        for element in order:
            result += "- " + element[0] + ": " + str(element[1])+ "\n"
            
        return result