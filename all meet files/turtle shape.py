import turtle
turtle.shape("square")
turtle.stamp()
turtle.shape("arrow")
turtle.fd(10)
turtle.stamp()

turtle.penup()
turtle.fd(20)
turtle.pendown()
for i in range(4):
    turtle.fd(20)
    turtle.right(90)
turtle.fd(20)
turtle.right(45)
for i in range(2):
    turtle.fd(20)
    turtle.right(110)
