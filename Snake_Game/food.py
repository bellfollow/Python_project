from turtle import Turtle
import random

class Food(Turtle): #Turtle 클래스 상속 받음
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self): #좌표 -280~280 사이 렌덤 난수 생성성
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
