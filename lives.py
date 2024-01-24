from turtle import Turtle


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.lives = 1
        self.update_lives()

    def loose_life(self):
        self.clear()
        self.lives -= 1
        self.update_lives()

    def update_lives(self):
        self.goto(500, 350)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 17, "normal"))
