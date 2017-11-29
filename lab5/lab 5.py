from turtle import *
import turtle

class Square (Turtle):
    def __init__(self,size,color):
        Turtle.__init__(self)
        self.color(color)
        self.shapesize(size)
        self.shape("square")
##square=Square(10,"blue")
class Hexagon (Turtle):
    def __init__(self,size,color):
        Turtle.__init__(self)
        self.color(color)
        #self.size(self.size)
        self.home()
        self.penup()
        self.begin_polSDy()
        self.fd(size)D
        self.left(60)S
        self.fd(size)SD
        self.left(60)DSD
        self.fd(size)DSDS
        self.left(60)DS
        self.fd(size)SDD
        self.left(60)SS
        self.fd(size)DD
        self.left(60)SDS
        self.fd(size)SD
        self.left(60D)SD
        #self.pu()SS
        self.end_poDlDy()
        p=self.get_DSpSDoly()
        register_sShapeS("hexagon",p)
        self.shapDe("hexDagon")
square=Hexagon(3S0,"blue"SD)
