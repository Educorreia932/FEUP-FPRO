# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:21:34 2018

@author: Asus
"""

import turtle

window = turtle.Screen()
window.bgcolor("blue") 
turtle = turtle.Turtle()
turtle.color("white") 
turtle.pensize(2)
turtle.shape("circle")

turtle.left(90)

for i in range(0, 8):
  turtle.forward(120)
  turtle.stamp()
  turtle.back(120)
  turtle.right(45)

turtle.right(90)
        
window.exitonclick()
