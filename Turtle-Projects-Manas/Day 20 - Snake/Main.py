from turtle import Screen
import time
from snake import  Snake
from food import Food
from score import Score
scr=Screen()
scr.listen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.tracer(0)

snake=Snake(3)
food = Food()
score=Score()
move_snake=False
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")
game_on=True

score.start_score()
def start_game():
    global move_snake,food,snake,game_on
    move_snake=True
    game_on=True
    snake.initialize()
    food.initialize()
    score.show_score()

def reset_game():
    snake.reset()

scr.onkey(start_game,"Return")



while game_on:
    scr.update()
    while move_snake:
        scr.update()
        snake.move_forward()
        time.sleep(0.1)
        # Detect collision with food
        if snake.head.distance(food) <15:
            food.refresh()
            score.increase_score()
            snake.increase_size()
        #Detect collision with wall
        if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
            move_snake=False
            game_on=False
            score.game_over()

        #Detect Collision with Tail
        for sp in snake.snake_parts[1:]:
            if snake.head.distance(sp)<10:
                move_snake=False
                game_on=False
                score.game_over()
    if not game_on:
        reset_game()
        game_on=True
    time.sleep(0.1)

scr.exitonclick()