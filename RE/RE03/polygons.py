import turtle

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.color("black")

for s in range(0, 4):
    turtle.left(90)
    turtle.forward(100)

for t in range(0, 3):
    turtle.left(120)
    turtle.forward(100)

for h in range(0, 6):
    turtle.left(60)
    turtle.forward(100)

for h in range(0, 8):
    turtle.left(45)
    turtle.forward(100)

window.exitonclick()
