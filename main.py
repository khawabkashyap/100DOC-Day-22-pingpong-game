from turtle import Turtle, Screen
from board import Board
import time

screen = Screen()
screen.title("Ping Pong")
screen.setup(width=800, height=600)
screen.bgcolor('Black')

r_board = Board(position=(380, 0))
l_board = Board(position=(-380, 0))

screen.listen()
screen.onkey(r_board.up, 'Up')
screen.onkey(r_board.down, 'Down')
screen.onkey(l_board.up, 'w')
screen.onkey(l_board.down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
