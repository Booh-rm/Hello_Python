import turtle
from turtle import *

def draw_dream():
    window = turtle.Screen()
    window.bgcolor("white")
    line()
    window.exitonclick()
    speed(0)

def line():

        turtle.left(380)
        turtle.forward(400)

draw_dream()