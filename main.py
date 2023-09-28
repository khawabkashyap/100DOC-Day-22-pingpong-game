from turtle import Turtle, Screen
from board import Board
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor('Black')
screen.tracer(0)

r_board = Board(position=(360, 0))
l_board = Board(position=(-360, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_board.up, 'Up')
screen.onkey(r_board.down, 'Down')
screen.onkey(l_board.up, 'w')
screen.onkey(l_board.down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with paddle or board
    if ball.distance(r_board) < 55 and ball.xcor() > 348 or ball.distance(l_board) < 55 and ball.xcor() < -348:
        ball.bounce_x()

    # Detect r-paddle miss
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.update_l_score()

    # Detect l-paddle miss
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.update_r_score()

screen.exitonclick()
