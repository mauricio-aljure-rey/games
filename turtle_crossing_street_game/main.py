import time
from turtle import Screen
import player
import car_manager
import scoreboard
from scoreboard import Scoreboard


def move_up_turtle():
    global player_released
    if player_released:
        if game_on:
            player_turtle.move_up()


# Constants
LINES_SIZE = 50
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_HEIGHT_LIMIT = SCREEN_HEIGHT - LINES_SIZE * 4

# Setting up the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()
screen.onkeypress(move_up_turtle, "Up")

# Setting up the player turtle
player_turtle = player.Player(GAME_HEIGHT_LIMIT, lines_size=LINES_SIZE)

# Setting up the car manager
car_manager = car_manager.CarManager(lines_size=LINES_SIZE,
                                     game_height_limit=GAME_HEIGHT_LIMIT,
                                     screen_width=SCREEN_WIDTH)

# setting the scoreboard
score_board = scoreboard.Scoreboard(game_height_limit=GAME_HEIGHT_LIMIT, lines_size=LINES_SIZE)

game_on = True
player_released_counter = 0
player_released = False

while game_on:
    # Updating routines
    time.sleep(0.1)
    screen.update()
    car_manager.update_cars()

    # Waiting for cars to populate the game
    player_released_counter += 1
    if player_released_counter > SCREEN_WIDTH/car_manager.cars_step:
        player_released = True

    # Checking if turtle has crossed
    if player_turtle.ycor() > GAME_HEIGHT_LIMIT/2:
        score_board.score_up()
        player_turtle.init_pos()
        car_manager.increase_speed()

    # Detecting collisions
    for car in car_manager.car_list:
        if player_turtle.ycor() == car.ycor():
            if abs(player_turtle.xcor() - car.xcor()) \
                    < car_manager.car_width/2 + player_turtle.shape_factor/2 * LINES_SIZE:
                # Collision occurred
                print("Collision occurred")
                game_on = False
                score_board.game_over()
                screen.update()

screen.exitonclick()