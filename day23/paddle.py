from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(3, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
