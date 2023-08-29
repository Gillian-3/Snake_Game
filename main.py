from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("MY ANACONDA")
screen.tracer(0)
anaconda=Snake()
food=Food()
score_board=ScoreBoard()
screen.listen()
screen.onkey(anaconda.up,"Up")
screen.onkey(anaconda.down,"Down")
screen.onkey(anaconda.left,"Left")
screen.onkey(anaconda.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    anaconda.move()
    if anaconda.head.distance(food)<20:
        anaconda.extend()
        food.refresh()
        score_board.increase_score()
    if anaconda.head.xcor()>280 or anaconda.head.xcor()<-280 or anaconda.head.ycor()>280 or anaconda.head.ycor()<-280:
        game_is_on=False
        score_board.game_over()
    for segment in anaconda.snake[1:]:
        if anaconda.head.distance(segment)<10:
            game_is_on=False
            score_board.game_over()

screen.exitonclick()