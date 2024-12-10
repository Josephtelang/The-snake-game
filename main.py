from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score_board

score = Score_board()
food = Food()
# create the snake game screen.
snake = Snake()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The snake game!")
List_of_starting_segment = [(0,0),(-20,0),(-40,0)]
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on = True

# move the snake.
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect the collision of food & extend the size of snake.
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend_snake()
        food.refresh()

    # Detect the collision with wall.
    if snake.head.xcor()>280 or snake.head.ycor()>299 or snake.head.xcor()<-280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()
        
    # Detect the collision of snake with body of the snake.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

   
screen.exitonclick()