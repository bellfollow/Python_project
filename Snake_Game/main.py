from turtle import Turtle,Screen
from snake import Snake
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

start_point = [(0,0),(-20,0),(-40,0)]
segments = []

snake = Snake()

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


screen.exitonclick()
