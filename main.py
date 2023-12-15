from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from deck import Deck
from score_counting import Score
import time

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
deck = Deck()
l_score = Score((-50, 200))
r_score = Score((50, 200))

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 \
            or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.x_bounce()

    if ball.xcor() > 400:
        ball.reset_position()
        l_score.score_increase()
        l_score.update_scoreboard()

    if ball.xcor() < -400:
        ball.reset_position()
        r_score.score_increase()
        r_score.update_scoreboard()

screen.exitonclick()