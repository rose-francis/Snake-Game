from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to snake game")
screen.tracer(0)

snakey=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snakey.up,"Up")
screen.onkey(snakey.down,"Down")
screen.onkey(snakey.right,"Right")
screen.onkey(snakey.left,"Left")

game_is_on=True
s=0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakey.move()

    
    if snakey.head.distance(food)<15:
        food.refresh()
        snakey.extend()
        s+=1
        score.clear()
        score.writes(s)
    
    if snakey.head.xcor()>280 or snakey.head.xcor()<-280 or snakey.head.ycor()>280 or snakey.head.ycor()<-280:
        game_is_on=False
        score.gameover()
        
    for segment in snakey.segments[1:]:
        if snakey.head.distance(segment)<10:
            game_is_on=False
            score.gameover()


screen.exitonclick()
