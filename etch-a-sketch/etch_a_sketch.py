from turtle import Turtle, Screen
conny=Turtle()
screen=Screen()
screen.listen()
def move_forward():
    conny.forward(10)
screen.onkey(fun=move_forward,key="w")
def move_backward():
    conny.backward(10)
screen.onkey(fun=move_backward,key="s")
def move_left():
    conny.left(10)
screen.onkey(fun=move_left,key="a")
def move_right():
    conny.right(10)
screen.onkey(fun=move_right,key="d")
def clear():
    conny.clear()
    conny.penup()
    conny.home()
screen.onkey(fun=clear,key="c")


screen.exitonclick()
