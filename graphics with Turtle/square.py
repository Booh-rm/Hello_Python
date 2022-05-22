from turtle import *
import turtle

def draw_dream():
    window = turtle.Screen()
    window.bgcolor("white")
    square(200)
    window.exitonclick()
    speed(0)

def square(longitud):

    for i in range(4):
        forward(longitud)
        right(90)

draw_dream()