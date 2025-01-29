from turtle import Turtle
ALIGN = "center"
FONT = ("Arial",24,"normal") 
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write_borad()

    def write_borad(self):
        self.write(f"Score : {self.score}", align = ALIGN, font = FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGN,font=FONT)

    def increase_socre(self):
        self.score += 1
        self.clear()
        self.write_borad()