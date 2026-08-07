from turtle import Turtle, Screen
import random
tim=Turtle()
screen=Screen()
tim.shape("triangle")
tim.color("Blue")
num_sides=2
colors=["red","blue","green","yellow","black","grey","teal","beige","brown","purple"]
for i in range(3,11):
    num_sides+=1
    tim.color(random.choice(colors))
    angles=360/num_sides
    for j in range(num_sides):
        tim.forward(100)
        tim.right(angles)
