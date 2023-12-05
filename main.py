# Welcome to snake game. Created by Dwi Didit Prasetiyo
from turtle import Screen
import time
#import snake class
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#create snake class
snake = Snake()

# control the snake
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

#create a food
food = Food()

#create a scoreboard
scoreboard = Scoreboard()


#move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        if scoreboard.score == 30:
            game_is_on = False
            scoreboard.win()


    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()

# exit on space bar
screen.exitonclick()

















