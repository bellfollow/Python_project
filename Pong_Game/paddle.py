from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,point):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,0.5)
        self.goto(point)
                  
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() -  20
        self.goto(self.xcor(), new_y)