from turtle import Turtle

ALLIGNMENT = "center"
FONT = ('courier', 80, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.dashed_line()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.r_paddle_score = 0
        self.l_paddle_score = 0
        self.create_score()

    def create_score(self):
        self.goto(100, 200)
        self.write(self.r_paddle_score, align=ALLIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.l_paddle_score, align=ALLIGNMENT, font=FONT)

    def update_r_score(self):
        self.clear()
        self.r_paddle_score += 1
        self.create_score()
        self.dashed_line()

    def update_l_score(self):
        self.clear()
        self.l_paddle_score += 1
        self.create_score()
        self.dashed_line()

    def dashed_line(self):
        self.pencolor("white")
        self.penup()
        self.pensize(8)
        self.hideturtle()
        self.goto(0, -300)
        while self.ycor() < 300:
            self.setheading(90)
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(20)
