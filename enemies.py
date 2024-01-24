import time
from turtle import Turtle


class Enemy(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("turtle")
        self.color("#4E9525")
        self.setheading(270)
        self.shapesize(stretch_len=1, stretch_wid=1.5)
        self.penup()
        self.goto(x_cor, y_cor)
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 100
        self.lower_wall = self.ycor() - 100


class Enemies:
    def __init__(self):
        self.y_start = 150
        self.y_end = 350
        self.enemies = []
        self.create_paths()
        self.move_x = .5
        self.move_y = .1

    def create_path(self, y_cor):
        for i in range(-150, 150, 70):
            enemy = Enemy(i, y_cor)
            self.enemies.append(enemy)

    def create_paths(self):
        for i in range(self.y_start, self.y_end, 45):
            self.create_path(i)

    def move_enemies_right_left(self):
        for i in range(5):
            for enemy in self.enemies:
                new_x = enemy.xcor() + self.move_x
                new_y = enemy.ycor() - self.move_y
                enemy.goto(new_x, new_y)
                if enemy.xcor() == 250:
                    self.move_x *= -1
                elif enemy.xcor() == -250:
                    self.move_x *= -1

    def move_down(self):
        time.sleep(1)
        self.move_y += .1

    def reset_enemies(self):
        for i in range(5):
            for enemy in self.enemies:
                # new_x = enemy.xcor() + self.move_x
                # new_y = enemy.ycor() - self.move_y
                enemy.goto(0, 350)
            self.move_enemies_right_left()




