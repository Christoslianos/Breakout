from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("brown")
        self.shape("square")
        self.shapesize(stretch_wid=0.85, stretch_len=3)
        self.penup()
        self.goto(position)