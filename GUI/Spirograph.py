import turtle
from turtle import Turtle, Screen
import random
tim=Turtle()
turtle.colormode(255)
screen=Screen()
tim.shape("triangle")
tim.color("Blue")
tim.speed(0)

def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
def spirograph(gap_size):

    for i in range(int(360/gap_size)):
        tim.circle(50)
        tim.color(random_color())

        tim.setheading(tim.heading()+gap_size)

spirograph(10)
screen.exitonclick()
