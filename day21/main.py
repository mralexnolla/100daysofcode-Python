from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("#thankU4Ex16 snake game")
screen.tracer(0)

# segmentList = []

# x = 0
# y = 0
#
# for i in range(0, 3):
#     segment = Turtle("square")
#     segment.color("white")
#     segment.penup()
#     segmentList.append(segment)
#
# for segment in segmentList:
#     segment.goto(x, y)
#     x -= 20

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for i in range(len(segmentList) - 1,0,-1):
    #     new_x = segmentList[i - 1].xcor()
    #     new_y = segmentList[i - 1].ycor()
    #     segmentList[i].goto(new_x, new_y)
    # segmentList[0].forward(20)
    # segmentList[0].left(90)
    snake.move()

screen.exitonclick()
