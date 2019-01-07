import turtle
import time
import random
import math
import Ball from ball.py
turtle.colormode(255)
turtle.tracer(0)
turtle.hideturtle()

global running = true
global screen_width, screen_height
screen_width = Turtle.getcanvas().winfo_height()/2
screen_height = Turtle.getcanvas().winfo_height()/2

numbers_of_balls = 5
maximum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5

balls = []
#If you want a random number between values a and b, call:
# random.randint(a, b)
for i in range number_of_balls:
    X = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
    Y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
    DX = random.randint(minimum_ball_dx,maximum_ball_radius)
    DX = random.randint(minimum_ball_dy,maximum_ball_radius)
    radius = random.randint(minimum_ball_radius, maximum_ball_radius)
    color = (random.random(),random.random(),random.random())
my_ball = Ball(X,Y,DX,DY,radius,color)
balls.append = my_ball

def move_all_balls():
    for i in range balls:
        move(
