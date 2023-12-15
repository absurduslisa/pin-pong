from turtle import Turtle, Screen
screen = Screen()

MOVE_DISTANCE = 20


class Deck(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 300)
        self.hideturtle()
        self.color('white')
        self.setheading(270)
        self.create_half()

    def create_half(self):
        for _ in range(0, 150):
            self.penup()
            self.forward(MOVE_DISTANCE)
            self.pendown()
            self.forward(MOVE_DISTANCE)
