# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:19:51 2018

@author: Asus
"""

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen") 
turtle = turtle.Turtle()
turtle.color("blue") 
turtle.pensize(3)
turtle.shape("turtle")

turtle.left(90)

for i in range(0, 12):
  turtle.penup()
  turtle.forward(90)
  turtle.pendown()
  turtle.forward(10)
  turtle.penup()
  turtle.forward(20)
  turtle.pendown()
  turtle.stamp()
  turtle.penup()
  turtle.back(120)
  turtle.right(30)

turtle.right(90)
        
window.exitonclick()