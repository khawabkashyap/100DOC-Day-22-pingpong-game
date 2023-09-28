from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movement_y = 10
        self.movement_x = 10

    def move(self):
        new_x = self.xcor() + self.movement_x
        new_y = self.ycor() + self.movement_y

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.movement_y *= -1

    def bounce_x(self):
        self.movement_x *= -1

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()
