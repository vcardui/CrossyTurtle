from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.start = STARTING_POSITION
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        self.goto(self.start)
        self.speed("fastest")

    def up(self):
        self.forward(MOVE_DISTANCE)
