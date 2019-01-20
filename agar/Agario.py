import turtle
import time
import random
import math
from ball import Ball
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()

running = True

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

numbers_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
my_ball=Ball(3,3,4,5,5,"yellow")
balls = []
#If you want a random number between values a and b, call:
# random.randint(a, b)
for i in range (numbers_of_balls):
    X = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
    Y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
    DX = random.randint(minimum_ball_dx,maximum_ball_radius)
    DY = random.randint(minimum_ball_dy,maximum_ball_radius)
    radius = random.randint(minimum_ball_radius, maximum_ball_radius)
    color = (random.random(),random.random(),random.random())
    other_ball = Ball(X,Y,DX,DY,radius,color)
    balls.append(other_ball)

def move_all_balls():
    for i in balls:
        i.move(screen_width,screen_height)
        
def collide(ball_a,ball_b):
    for i in balls:
        if ball_a==ball_b:
            return False
        else:
            print("ball a equals to ball_b")
            distance = math.sqrt((balls[i+1].x - balls[i].x)+ (balls[i+1].y - balls[i].y))
            if distance < 0:
                print("line 48")
                return True
            else:
                return False
        
def check_all_balls_collision():
    all_balls=[]
    all_balls.append(my_ball)
    for ball in balls:
        all_balls.append(ball)

    for ball_a in all_balls:
        for ball_b in all_balls:
            if collide(ball_a,ball_b):
                r1 = ball_a.r
                r2 = ball_b.r
                X_coordinate = random.randint(0,screen_width)
                Y_coordinate = random.randint(0,screen_height)
                X_AxisSpeed = random.randint(minimum_ball_dx , maximum_ball_dx)
                while ball_a.dx == 0:
                    ball_a.dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                while ball_a.dy == 0:
                    self.dy = random.randint(minimum_ball_dy , maximum_ball_dy)
                radius = random.randint(0,3)
                color = (random.random(),random.random(),random.random())

                if ball_a == my_ball:
                    print("GameOver")
                    quit()
               
                if ball_a.r < ball_b:
                    ball_a.new_Ball(X,Y,DX,DY,radius,color)
                    ball_b.r += 1
def move_around():
    X_Coordinate = turtle.getcanvas().winfo_pointerx() - screen_width
    Y_Coordinate = screen_height - turtle.getcanvas().winfo_pointery()
    my_ball.x = X_Coordinate
    my_ball.y = Y_Coordinate

while running:
    if not screen_width == turtle.getcanvas().winfo_width() and screen_height == turtle.getcanvas().winfo_height():
        screen_width = turtle.getcanvas().winfo_width()/2
        screen_height = turtle.getcanvas().winfo_height()/2
    move_around()
    move_all_balls()
    check_all_balls_collision()
