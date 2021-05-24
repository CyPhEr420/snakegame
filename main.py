from turtle import Screen
from snake import Snake
import time
from scorebord import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()
screen.listen()

screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.right, key="Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score_board.reset_screen()
        snake.reset_snake()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset_screen()
            snake.reset_snake()
screen.mainloop()
