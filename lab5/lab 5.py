from turtle import *
import turtle
class Square (Turtle):
    def __init__(self,size,color):
        Turtle.__init__(self)
        self.color(color)
        self.shapesize(size)
        self.shape("square")
##square=Square(10,"blue")
turtle.register_shape("hexagon",((50,50),(75,60),(50,30),(25,20),(10,10)) 
class Hexagon (Turtle):
    def __init__(self,size,color):
        Turtle.__init__(self)
        self.color(color)
        self.shapesize(size)
        self.shape("hexagon")
square=Hexagon(10,"blue")
