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
    draw_head(brad)
 
def draw_head(brad):
    brad.circle(90)
    brad.speed(0)
    brad.right(60)
 
draw_dream()