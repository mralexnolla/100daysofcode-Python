from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("White")
        # self.write(f"Score: {self.score}", align="center", font=("arial", 24, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f" #thankU4Ex16 Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align=ALIGNMENT, font=FONT)