from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_raceOn = False

user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win, Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x = -240
y = -100
turtle_list = []

for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 40
    turtle_list.append(new_turtle)


if user_bet:
    is_raceOn = True

while is_raceOn:
    for turtle in turtle_list:
        race_distance = random.randint(0, 10)
        turtle.forward(race_distance)
        if turtle.xcor() > 225:
            is_raceOn = False
            wining_color = turtle.pencolor()
            if user_bet == wining_color:
                print("You won")
            else:
                print(f"you lost. The winning turtle is {wining_color}")




screen.exitonclick()