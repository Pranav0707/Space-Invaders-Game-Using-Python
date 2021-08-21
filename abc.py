import turtle
bob=turtle.Turtle()
bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.color("red")
bob.speed(10)
for i in range(100):
    bob.forward(50)
    bob.left(250)
    bob.forward(50)
