from turtle import *
import turtle
import time
import random
from Ball import Ball
import math
turtle.tracer(delay=0)    
turtle.hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2 
MY_BALL = Ball("circle","red",100,100,0,0,30)
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MAXIMUM_BALL_DY=5
MINIMUM_BALL_DY=-5
BALLS=[]
turtle.pu()
for i in range (NUMBER_OF_BALLS):
    radius=random.randint(round(MINIMUM_BALL_RADIUS),round(MAXIMUM_BALL_RADIUS))
    x=random.randint(round(-SCREEN_WIDTH)+round(MAXIMUM_BALL_RADIUS),round(SCREEN_WIDTH)-round(MAXIMUM_BALL_RADIUS))
    y=random.randint(round(-SCREEN_HEIGHT)+round(MAXIMUM_BALL_RADIUS),round(SCREEN_HEIGHT)-round(MAXIMUM_BALL_RADIUS))
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    while dx == 0 and dy == 0:
        dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
        dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    color=(random.random(), random.random(), random.random())
    new_ball=Ball("circle",color,x,y,dx,dy,radius)
    BALLS.append(new_ball)
def move_all_balls():
    for new_ball in BALLS:
        new_ball.Move(SCREEN_WIDTH,SCREEN_HEIGHT)
def collide(ball_a,ball_b):
    if ball_a==ball_b:
        return False
    distance=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if(distance+10<ball_a.r+ball_b.r):
        return True
    else:
        return False
def check_all_balls_collisions():
    for ball_b in (BALLS):
        for ball_a in(BALLS):
            if collide(ball_a,ball_b)==True:
                ball_a_radius=ball_a.r
                ball_b_radius=ball_b.r
            X_CORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
            Y_CORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
            X_AXISSPEED=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
            Y_AXISSPEED=random.randint(MAXIMUM_BALL_DY,MAXIMUM_BALL_DY)
            while  X_AXISSPEED or Y_AXISSPEED == 0:
                X_AXISSPEED=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                Y_AXISSPEED=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
            radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
            color=(random.random(),random.random(),random.random())
            if ball_a.r>ball_b.r:
                ball_b.r=radius
                ball_b.goto(X_CORDINATE,Y_CORDINATE)
                ball_b.dx+X_AXISSPEED
                ball_b.dy=Y_AXISSPEED
                ball_b.color(color)
                ball_b.shapesize(ball_b.r/10)
                ball_a.r=ball_a.r+2
                ball_a.shapesize(ball_a.r/10)
            else:
                ball_a.r=radius
                ball_a.goto(X_CORDINATE,Y_CORDINATE)
                ball_a.dx=X_AXISSPEED
                ball_a.dy=Y_AXISSPEED
                ball_a.color(color)
                ball_a.shapesize(ball_a.r/10)
                ball_b.r=ball_a.r+2
                ball_b.shapesize(ball_b.r/10)
def check_myball_collision():
    for ball in BALLS:
        if collide(MY_BALL,ball)==True:
            Y_AXISSPEED=random.randint(round(MINIMUM_BALL_DY),round(MAXIMUM_BALL_DY))
            X_AXISSPEED=random.randint(round(MINIMUM_BALL_DX),round(MAXIMUM_BALL_DX))
            Y_CORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
            X_CORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
            while X_AXISSPEED and Y_AXISSPEED ==0:
                Y_AXISSPEED=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                X_AXISSPEED=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
            radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
            color=(random.random(),random.random(),random.random())
            if MY_BALL.r>ball.r:
                ball.r=radius
                ball.x=X_CORDINATE
                ball.y=Y_CORDINATE
                ball.goto(X_CORDINATE,Y_CORDINATE)
                ball.dy=Y_AXISSPEED
                ball.dx=X_AXISSPEED
                ball.color(color)
                ball.shapesize(ball.r/10)
                MY_BALL.r+=2
                MY_BALL.shapesize(MY_BALL.r/10)
            else:
                return False
    return True
def movearound(event):
    MY_BALL.goto(event.x -SCREEN_WIDTH,SCREEN_HEIGHT-event.y)



turtle.getcanvas().bind("<Motion>",movearound)
turtle.listen()
while RUNNING==True:
    move_all_balls()
    check_all_balls_collisions()
    MY_BALL.Move(SCREEN_WIDTH,SCREEN_HEIGHT)
    RUNNING = check_myball_collision()
    turtle.update()
    time.sleep(SLEEP)
    #turtle.mainloop()
    
