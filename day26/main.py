import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("Regions of Ghana")
image = "./Ghana_map1.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("./16_regions.csv")

regions = data["regions"].tolist()

guessed_regions = []

while len(guessed_regions) < 16:
    answer_region = screen.textinput(f"{len(guessed_regions)}/16 Regions correct", "Whats the next one").title()

    if answer_region == "Exit":
        missing_regions = []
        for region in regions:
            if region not in guessed_regions:
                missing_regions.append(region)
        newData = pandas.DataFrame(missing_regions)
        newData.to_csv("./regions_to_learn.csv")
        break
    if answer_region in regions:
        guessed_regions.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.regions == answer_region]
        x = row.x.iloc[0]
        y = row.y.iloc[0]
        t.goto(x, y)
        t.write(row.regions.iloc[0], align="left", font=("Arial", 16, "bold"))

# regions_to_learn.csv


# turtle.mainloop()
# screen.exitonclick()
