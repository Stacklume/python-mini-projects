from turtle import Turtle, Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your choice", prompt="Which turtle will win the race? Enter a color:")
print(user_bet)
race_on=False
colors=["red","orange","yellow","green","blue","purple"]
all_turtles=[]

for color in colors:
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230,y=colors.index(color)*-30+90)
    all_turtles.append(new_turtle)

if user_bet:
    race_on=True

while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            race_on=False
screen.exitonclick()