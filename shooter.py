from turtle import Turtle


class Shooter(Turtle):
    def __init__(self, shape, color, stretch_width, stretch_length, position):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.shapesize(stretch_wid=stretch_width, stretch_len=stretch_length)
        self.penup()
        self.goto(position)
        self.pace = 50
        self.move_y = 20
        self.ball_speed = 2
        self.shooter_position = 0

    def go_right(self):
        new_x = self.xcor() + self.pace
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - self.pace
        self.goto(new_x, self.ycor())

    def reset_shooter(self):
        self.goto(0, -350)

    def move_upward(self):
        new_y = self.ycor() + self.move_y * self.ball_speed
        self.goto(self.xcor(), new_y)

    def move_downward(self):
        new_y = self.ycor() - self.move_y * self.ball_speed
        self.goto(self.xcor(), new_y)

