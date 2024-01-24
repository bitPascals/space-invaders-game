from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
        with open("highest_score.txt") as data:
            self.highest_score = int(data.read())

    def update_scoreboard(self):
        self.clear()
        self.goto(-500, 350)
        self.write(f"Score: {self.score} ", align="center", font=("Courier", 14, "normal"))

    def increase_score(self):
        self.score += 5
        self.update_scoreboard()

    def update_highest_score(self):
        if int(self.score) > self.highest_score:
            self.highest_score = int(self.score)
            with open("highest_score.txt", "w") as data:
                data.write(f"{self.highest_score}")
        self.goto(-150, 350)
        self.write(f"Highest Score: {self.highest_score}", align="center", font=("Courier", 17, "normal"))









