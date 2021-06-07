# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:34:54 2018

@author: Asus
"""

def fight(heroes, villain):
    heroes = list(filter(lambda a: a["category"] == villain["category"], heroes))
    
    for hero in heroes:
        if hero["health"] >= villain["health"]:
            hero["score"] += 1
            return hero["name"] + " defeated the villain and now has a score of " + str(hero["score"])
        
        else:
            villain["health"] += - hero["health"] / 2
            
    return villain["name"] + " prevailed with " + str(villain["health"]) + "HP left"