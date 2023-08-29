from turtle import Turtle
ALIGNMENT="center"
FONT_TUPLE=("Arial", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.write(f"Score Board: {self.score}", align=ALIGNMENT, font=FONT_TUPLE)
    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_TUPLE)