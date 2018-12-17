import turtle
i1=1
turtle.speed(0)
for i in range(360):
    turtle.fd(100)
    turtle.right(45)
    turtle.fd(200)
    turtle.right(45)
    turtle.fd(50)
    turtle.home()
    turtle.right(i1)
    i1=i1+1
    
