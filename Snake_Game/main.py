from turtle import Turtle,Screen
from food import Food
from snake import Snake
import time
from score_board import Score_Board


#게임 실행 화면 구성 600 * 600이고 배경이 black
screen = Screen() 
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0) #애니메이션 제어 함수로 애니메이션을 on/off할 수 있음
                #n이 제공된다면 n번째 정기 화면 갱신만 실제로 수행함
                #n과 delay값을 변수로 받을 수 있음



start_point = [(0,0),(-20,0),(-40,0)] #뱀의 각각의 머리 부분의 시작 좌표
segments = []

snake = Snake() #몸통 제어 관련 클래스 -> snake.py에서 살펴보자자
food = Food() #스코어를 올려주는 먹이 관련 클래스
scoreboard = Score_Board() #점수가 올라가는 것을 보는 보드
screen.listen() #키 이벤트 수집을 위해 사용되는 라이브러리로 onkey을 onclick 메서드에 전달 할 수 있는 더미 인자가 제공됨
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update() #위의 Screen 갱신을 수행함
    time.sleep(0.1) 
    #대가리를 따라가는 몸통
    snake.move()    

    #음식과 닿는 것을 감지
    if snake.head.distance(food) < 15:
        print("냐암 냐암 냐암")
        food.refresh()
        scoreboard.increase_socre()
        snake.extend()

    # 대가리 벽에 닿으면 종료
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # 아래 코드를 보다 간결하게 작성해보기
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False    
    #         scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # #대가리 꼬리에 닿으면 종료

screen.exitonclick()
