from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red", "green")

def move_forward():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def move_up():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_down():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key="Right", fun=move_forward)
screen.onkey(key="Left", fun=move_backwards)
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)
screen.onkey(key="c", fun=clear)



screen.exitonclick()
