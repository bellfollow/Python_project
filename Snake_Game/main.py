from turtle import Turtle,Screen
from food import Food
from snake import Snake
import time
from score_board import Score_Board

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

start_point = [(0,0),(-20,0),(-40,0)]
segments = []

snake = Snake()
food = Food()
scoreboard = Score_Board()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while True:
    screen.update()
    time.sleep(0.1)
    #대가리를 따라가는 몸통
    snake.move()    

    #음식과 닿는 것을 감지
    if snake.head.distance(food) < 15:
        print("냐암 냐암 냐암")
        food.refresh()
        scoreboard.increase_socre()

screen.exitonclick()
