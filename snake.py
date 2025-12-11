from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
       
    
    def add_segment(self,pos):
        new=Turtle()
        new.shape("square")
        new.color("white")
        new.penup()
        new.setpos(pos)
        self.segments.append(new)

    def extend(self):
        pos=self.segments[-1].position()
        self.add_segment(pos)
                

    def move(self):
        for pos in range(len(self.segments)-1,0,-1):
            new_x=self.segments[pos-1].xcor()
            new_y=self.segments[pos-1].ycor()
            self.segments[pos].goto(new_x,new_y)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
