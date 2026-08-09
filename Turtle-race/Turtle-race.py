from turtle import Turtle,Screen
import random
race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make a bet",prompt="Which turtle according to you is going to win the race? Enter a color: " )
print(user_bet)
colors=["red","green","teal","brown","black","red"]
y_pos=[-100,-70,-40,-10,20,50]
all_turtle=[]
for t in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[t])
    all_turtle.append(new_turtle)
if user_bet:
    race_on=True
while race_on:
    for t in all_turtle:
        if t.xcor()>230:
            race_on=False
            winning_color=t.pencolor()
            if winning_color==user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")
        dist=random.randint(0,10)
        t.forward(dist)
screen.exitonclick()
