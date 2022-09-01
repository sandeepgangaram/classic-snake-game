from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

my_snake = Snake()
food = Food()
score = ScoreBoard()

screen.update()

screen.listen()

screen.onkeypress(my_snake.up, 'Up')
screen.onkeypress(my_snake.down, 'Down')
screen.onkeypress(my_snake.left, 'Left')
screen.onkeypress(my_snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move_snake_forward()

    # Detect collision
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend_snake()
        score.increase_score()

    # Watch for wall crash
    x = my_snake.head.xcor()
    y = my_snake.head.ycor()
    # if x > 280 or x < -280 or y > 280 or y < -280:
    if abs(x) > 280 or abs(y) > 280:
        game_is_on = False
        score.game_over()

    # Detect hitting tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    # for segment in my_snake.segments:
        # if segment == my_snake.head:
        #     pass
        # elif my_snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     score.game_over()

screen.exitonclick()
