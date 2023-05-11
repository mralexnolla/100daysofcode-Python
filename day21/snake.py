from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360


class Snake:

    def __init__(self):
        self.segmentList = []
        self.create_snake()
        self.move()
        self.head = self.segmentList[0]
        self.up()
        self.down()
        self.left()
        self.right()

    def create_snake(self):
        x = 0
        y = 0

        for i in range(0, 3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            self.segmentList.append(segment)

        for segment in self.segmentList:
            segment.goto(x, y)
            x -= 20

    def move(self):
        for i in range(len(self.segmentList) - 1, 0, -1):
            new_x = self.segmentList[i - 1].xcor()
            new_y = self.segmentList[i - 1].ycor()
            self.segmentList[i].goto(new_x, new_y)

        self.segmentList[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


