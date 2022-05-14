from turtle import Turtle


# create paddle class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_len=4, stretch_wid=1)  # the paddle has 20, 20 length
        self.penup()
        self.goto(position)

    # move paddle
    def go_right(self):
        if self.xcor() < 250:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -250:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

