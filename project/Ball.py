from turtle import Turtle
import turtle
import time
import random


##class Ball(Turtle):
##    def __init__(self,x,y,dx,dy,r,color):
##        self.x=x
##        self.y=y
##        self.dx=dx
##        self.dy=dy
##        self.r=r
##        self.color=color
##        Turtle(self):
##                 self.color(color)
##                 self.shape("circle")
##                 self.size(r/10)





RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

class Ball(Turtle):
        def __init__(self,shape,color,x,y,dx,dy,r):
            Turtle.__init__(self)
            self.x=x
            self.y=y
            self.color(color)
            self.shape(shape)
            self.penup()
            self.setpos(x,y)
            self.shapesize(r/10)
            self.dx=dx
            self.dy=dy
            self.r=r

        def Move(self,screen_width,scree_height):
            current_x=self.xcor()
            new_x=current_x+self.dx
            current_y=self.ycor()
            new_y=current_y
            right_side_ball=new_x+self.r
            top_side_ball=new_y+self.r
            left_side_ball=new_x-self.r
            bottom_side_ball=new_y-self.r
            self.goto(new_x,new_y)
            if(right_side_ball<screen_width/2):
                    pass
            else:
                    self.dx = -self.dx
                    
                    
                
