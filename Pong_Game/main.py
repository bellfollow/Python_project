#화면 너비는 800 높이는 600
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
scoreboard = ScoreBoard()

r_padle = Paddle((350,0))
l_padle = Paddle((-350,0))

# paddle1 = Turtle()
# paddle1.penup()
# paddle1.shape("square")
# paddle1.color("white")
# paddle1.shapesize(5,1)
# paddle1.goto(350,0)

# def go_up():
#     new_y = paddle1.ycor() + 20
#     paddle1.goto(paddle1.xcor(), new_y)

# def go_down():
#     new_y = paddle1.ycor() -  20
#     paddle1.goto(paddle1.xcor(), new_y)
ball = Ball()

screen.listen()
screen.onkey(r_padle.go_up ,"Up")
screen.onkey(r_padle.go_down ,"Down")

screen.onkey(l_padle.go_up ,"w")
screen.onkey(l_padle.go_down ,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        #바운스 필요wwwwwww
        ball.bounce_y()
    #오른쪽 패들 충ㅇ돌
    if (ball.distance(r_padle) < 40 and ball.xcor() > 320) or (ball.distance(l_padle) < 40 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()

    
screen.exitonclick()