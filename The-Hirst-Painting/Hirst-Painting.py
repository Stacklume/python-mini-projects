import turtle,random
from turtle import Turtle,Screen
turtle.colormode(255)
color_list=[(236, 235, 234), (232, 233, 238), (234, 238, 236), (237, 226, 231), (206, 164, 113), (19, 26, 53), (139, 63, 93), (226, 207, 133), (203, 134, 149), (207, 81, 106), (66, 94, 135), (85, 115, 97), (132, 153, 142), (65, 21, 39), (122, 35, 57), (142, 157, 174), (42, 53, 102), (140, 75, 58), (224, 181, 166), (225, 168, 182), (95, 126, 169), (111, 136, 124), (182, 188, 206), (179, 106, 98), (37, 83, 62), (204, 119, 46), (184, 197, 190), (32, 63, 48), (98, 50, 39), (69, 32, 22)]

tim=Turtle()
tim.setheading(225)
tim.hideturtle()
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.speed(0)
num_of_dots=100

for dot_count in range(1,num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=Screen()
screen.exitonclick()
