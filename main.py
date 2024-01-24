import time
import tkinter
import turtle
from random import randint
from turtle import Screen
from shooter import Shooter
from enemies import Enemies
from scoreboard import Scoreboard
from lives import Lives

# Setting up the screen
screen = Screen()
screen.bgcolor("#0F0F0F")
screen.setup(width=1300, height=760)
screen.title("Space Invaders")
screen.tracer(0)

# Setting up game objects
shooter = Shooter(shape="square", color="#A7D82E", stretch_width=1, stretch_length=1, position=(0, -350))
bullet = Shooter(shape="circle", color="white", stretch_width=.4, stretch_length=.2, position=(0, -320))
enemy_bullet = Shooter(shape="circle", color="#4E9525", stretch_width=.4, stretch_length=.2, position=(0, 60))
enemies = Enemies()
scoreboard = Scoreboard()
lives = Lives()

# Event listeners for keyboard keys
screen.listen()
screen.onkey(shooter.go_right,  "Right")
screen.onkey(shooter.go_left, "Left")


# Reshoot function for shooter
def reshoot():
    reset_bullet()
    bullet.move_upward()


# Reshoot function for enemy
def enemy_reshoot():
    reset_enemy_bullet()
    enemy_bullet.move_downward()


# Bullet reset function
def reset_bullet():
    bullet.goto(shooter.pos())


# Enemy bullet reset function
def reset_enemy_bullet():
    for enemy in enemies.enemies:
        enemy_bullet.goto(randint(-20, 0), randint(0, 20))


game_is_on = True
running = True

while game_is_on and running:
    if running:
        # This error exception deals with the turtle.Terminator error
        try:
            time.sleep(0.1)
            screen.update()
        except turtle.Terminator:
            break
        # This error exception handles the tkinter.TclError
        try:
            # This handles the bullet from the shooter
            bullet.move_upward()
            # This handles the bullet from the enemies
            enemy_bullet.move_downward()
            if enemy_bullet.ycor() < -350:
                enemy_reshoot()
        except tkinter.TclError:
            break
        for enemy in enemies.enemies:
            # Detecting bullet collision with the enemy
            if bullet.distance(enemy) < 20:
                enemy.hideturtle()
                enemies.enemies.remove(enemy)
                scoreboard.increase_score()
                reshoot()
            scoreboard.update_highest_score()
            if enemy_bullet.distance(shooter) < 30 and enemy_bullet.ycor() < -337 or enemy.distance(shooter) < 60:
                lives.loose_life()
                game_is_on = False
                lives.clear()
                lives.write(f"Game Over!", align="center", font=("Courier", 17, "normal"))
            if not enemies.enemies:
                lives.write(f"You win!", align="center", font=("Courier", 17, "normal"))
            elif bullet.ycor() > 350:
                reshoot()
        enemies.move_enemies_right_left()
    else:
        running = False
        game_is_on = False

screen.mainloop()

