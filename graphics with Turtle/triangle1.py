import turtle
 
def draw_dream():
    window = turtle.Screen()
    window.bgcolor("white")
    draw_Scarlett()
    window.exitonclick()
 
 
def draw_Scarlett():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    draw_triangle(brad)
 
def draw_triangle(brad):
    num = 0
    while num < 3:
        brad.forward(190)
        brad.right(120)
        brad.speed(1)
        num += 1

draw_dream()