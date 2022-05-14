import random
import turtle
from turtle import Screen, update, Turtle
from bricks import Brick
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

import time

# create the screen
screen = Screen()
screen.bgcolor('pink')
screen.setup(width=600, height=600)
screen.title("Breakout")
screen.tracer(0)

LIVE= 3

def life():
    turtle.clear()
    turtle.penup()
    turtle.color("white")
    turtle.hideturtle()
    turtle.goto(-260, 270)
    turtle.write(f'Life:{LIVE}', align="left",font=("Courier", 20, "normal"))


life()

# Create the brick wall
brick_horizontal = -250
brick_vertical = 250
bricks = []

for i in range(5):
    for j in range(8):
        brick = Brick((brick_horizontal, brick_vertical))
        bricks.append(brick)
        brick_horizontal += 65
    brick_horizontal = -250
    brick_vertical -= 20

d_paddle = Paddle((0, -250))
# create a ball
ball = Ball((0, -200))
# create a scoreboard
scoreboard = Scoreboard()
screen.listen()
screen.onkey(d_paddle.go_right, "Right")
screen.onkey(d_paddle.go_left, "Left")


start_game = True
while start_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the  celling
    if ball.ycor() > 270:
        # need sto bounce
        ball.bounce_y()
        # detect collision with the side walls
    if ball.xcor() > 270 or ball.xcor() < -270:
        ball.bounce_x()
        # detect collision with the d_paddle
    if ball.distance(d_paddle) < 35 and ball.ycor() > -250:
        ball.bounce_y()
        # detect collision with brick
    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.new_point()
    # detect when the player loses
    if ball.ycor() < -270:
        ball.reset_position()
        LIVE -= 1
        life()
    if LIVE == 0:
        start_game = False
        scoreboard.game_over()
    # detect when the paler wins
    if not bricks:
        start_game = False
        scoreboard.win()

update()


screen.exitonclick()
