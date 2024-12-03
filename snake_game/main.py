# Game Devloped from online course

import turtle
import time
import snake_class
import food
import scoreboard

screen_width = 1600 # pixels
screen_height = 800 # pixels
screen_udpate_time = 0.1 # seconds
repeat_game_forever = True


def onkey_up():
    if game_on:
        snake.up()
        screen.update()


def onkey_down():
    if game_on:
        snake.down()
        screen.update()


def onkey_left():
    if game_on:
        snake.left()
        screen.update()


def onkey_right():
    if game_on:
        snake.right()
        screen.update()


def end_game():
    global game_on
    game_on = False


# Setting up the screen
screen = turtle.Screen()
game_width_limit = round(screen_width*0.9)
game_height_limit = round(screen_height*0.9)
game_on = True

screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkeypress(end_game, "Escape")

limits = turtle.Turtle()
limits.color("white")
limits.penup()
limits.goto(-game_width_limit/2, -game_height_limit/2)
limits.pendown()
limits.goto(-game_width_limit/2, game_height_limit/2)
limits.goto(game_width_limit/2, game_height_limit/2)
limits.goto(game_width_limit/2, -game_height_limit/2)
limits.goto(-game_width_limit/2, -game_height_limit/2)
limits.hideturtle()

# Setting up the snake
snake_parts_size = 40
snake = snake_class.Snake(snake_parts_size=snake_parts_size)
screen.onkeypress(onkey_up, "Up")
screen.onkeypress(onkey_down, "Down")
screen.onkeypress(onkey_right, "Right")
screen.onkeypress(onkey_left, "Left")

# Setting up the food
food_size = snake_parts_size
food = food.Food(game_height_limit=game_height_limit, game_width_limit=game_width_limit,
                 snake_parts_size=snake_parts_size, food_size=food_size, snake=snake)

# Setting up the scoreboard
score_board = scoreboard.ScoreBoard(screen_height=screen_height)

# Running the game
while game_on:
    snake.move()
    screen.update()
    time.sleep(screen_udpate_time)

    # Eating food
    if snake.snake_parts[0].distance(food) < snake_parts_size/2 + food_size:
        food.move(snake)
        snake.extend_snake(snake.snake_parts[-1].position())
        score_board.score_up()

    # Collision with wall
    tol = snake_parts_size / 1.5
    if abs(snake.snake_parts[0].xcor()) > game_width_limit/2 - tol or \
            abs(snake.snake_parts[0].ycor()) > game_height_limit/2 - tol:
        game_on = False
        score_board.game_over()
        print('Snake touched a wall')

    # Collisions with tail
    for part in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(part) < snake_parts_size * 0.8:
            game_on = False
            score_board.game_over()
            print('Snake ate itself')

    # Reeating game for ever
    if game_on is False and repeat_game_forever == True:
        time.sleep(3)
        for part in snake.snake_parts:
            part.clear()
            part.ht()
        snake.snake_parts.clear()


        # snake.snake_parts.clear()
        score_board.score = 0
        snake.initialize()
        score_board.clear()
        score_board.goto(0, round(screen_height / 2 * 0.9))

        game_on = True






screen.exitonclick()

