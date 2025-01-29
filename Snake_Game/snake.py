from turtle import Turtle
START_POINTS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = [] #좌표 추가
        self.create_snake() 
        self.head = self.segments[0] #머리 위치치

    def create_snake(self): #뱀 만들기
        for point in START_POINTS: #모든 시작 포인트의 
            self.add_segment(point) #좌표 전달

    def add_segment(self,point): #
        new_seg = Turtle("square") #모양 사각형
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(point) #해당 좌표로 터틀 이동
        self.segments.append(new_seg) #해당 좌표 세그먼트 추가 
    #길이 늘리기
    def extend(self):
        self.add_segment(self.segments[-1].position())#position 거북이의 현재 위치 좌표를 반환합니다. 세그먼트 마지막 부분에 추가 

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):#뒤에서 0까지 뒤로 한칸씩 조지면서 for루프 돌리기
            new_x = self.segments[seg_num - 1].xcor() #xcor는 거북이의 x좌표를 반환
            new_y = self.segments[seg_num - 1].ycor() #y좌표를 반환
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE) 
    
    def up(self):
        if self.head.heading() != DOWN: #heading() 거북이의 현재 방향을 반환함
            self.head.setheading(UP)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:        
            self.head.setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    