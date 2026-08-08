from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
def move_forward():
    tim.forward(10)
def move_back():
    tim.back(10)
def counter_clock():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
