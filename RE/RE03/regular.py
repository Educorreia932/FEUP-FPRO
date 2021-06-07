import turtle

window = turtle.Screen()
turtle = turtle.Turtle()
sides_number = int(input("Choose the number of the sides of the polygon: "))
side_length = int(input("Choose the length of the side of the polygon: "))
turtle.color(input("Choose the border color: "), input("Choose the fill color: ")) 

turtle.begin_fill()

for i in range(0, sides_number + 1):
  turtle.forward(side_length)
  turtle.right(360 / (sides_number))
  
turtle.end_fill()
  
window.exitonclick()
