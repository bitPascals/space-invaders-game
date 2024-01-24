from turtle import Turtle


class ShooterBullet(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("#BED754")
        self.shapesize(stretch_len=.2, stretch_wid=.3)
        self.penup()
        self.goto(position)
        self.move_y = 100
        self.ball_speed = 0.1

    def move_upward(self):
        new_y = self.ycor() + self.move_y * self.ball_speed
        self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto(0, -300)

