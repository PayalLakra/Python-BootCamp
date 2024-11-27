from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super.__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(350,0)

def go_up(self):
    new_y = self.ycor() + 20
    paddle.goto(self.xcore(), new_y)

def go_down(self):
    new_y = self.ycor() - 20
    paddle.goto(.xcore(), new_y)