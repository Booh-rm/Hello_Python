import turtle
from turtle import *

def draw_dream():
    window = turtle.Screen()
    window.bgcolor("white")
    linea()
    window.exitonclick()
    speed(0)

def linea():
        
        turtle.forward(300)
        turtle.left(125)
        turtle.forward(300)
        turtle.left(117)
        turtle.forward(290)
     
draw_dream()