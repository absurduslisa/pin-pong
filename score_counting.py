from turtle import Turtle, Screen
screen = Screen()


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.position = position
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(self.position)
        self.write(arg=self.score, move=False, align='center', font=('Courier', 80, 'normal'))

    def score_increase(self):
        self.score += 1