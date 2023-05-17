from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scourboard()

    def update_scourboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def new_level(self):
        self.level += 1
        self.update_scourboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=FONT)
