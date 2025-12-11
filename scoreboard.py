from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",13,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.writes(0)
    
    def writes(self,s):
        self.write(f"Score:{s}",False,align=ALIGNMENT,font=FONT)
    
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",False,align=ALIGNMENT,font=("Arial",25,"normal"))