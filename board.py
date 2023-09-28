from turtle import Turtle


class Board(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        up_y = self.ycor() + 20
        self.goto(self.xcor(), up_y)

    def down(self):
        down_y = self.ycor() - 20
        self.goto(self.xcor(), down_y)

    def increase_score(self):
        self.score_count += 1
