import turtle

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,100) 
turtle.goto(-150,-100) 
turtle.goto(-100,100)
turtle.goto(-100,-100)
#drawing and E
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.goto(0,100)

turtle.goto(100, 100)
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.goto(0,0)
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(0,-100)

turtle.penup()
turtle.goto(300, 100)
turtle.pendown()
turtle.goto(200,100)
turtle.goto(200,-100)
turtle.goto(300,-100)
turtle.penup()
turtle.goto(300,0)
turtle.pendown()
turtle.goto(200,0)

turtle.penup()
turtle.goto(400,0)
turtle.pendown()
turtle.goto(400,-100)
turtle.goto(400,100)
turtle.goto(350,100)
turtle.goto(450,100)
