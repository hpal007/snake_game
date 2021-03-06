from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time
import os
import sys

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def restart_game():
    os.execv(sys.executable, ['python'] + sys.argv)


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# restart game
screen.onkey(restart_game, 'space')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect the collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        food.color_generator()

    # Detect collision on the wall.

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 260 or snake.head.ycor() < -290:
        scoreboard.chance_left -= 1
        scoreboard.reset()
        snake.reset()

    # Detect collision on with the tail.
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.chance_left -= 1
            scoreboard.reset()
            snake.reset()

    if scoreboard.chance_left == 0:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
