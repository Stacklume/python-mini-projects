import turtle
from turtle import Turtle, Screen
import random
tim=Turtle()
turtle.colormode(255)
screen=Screen()
tim.shape("triangle")
tim.color("Blue")
num_sides=2

def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
tim.width(10)
tim.speed(0)
directions=[0,90,180,270]
for i in range(100):
    tim.forward(60)
    tim.setheading(random.choice(directions))
    tim.color(random_color())
screen.exitonclick()
