import turtle
import paddle
import ball
import time
import scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_WIDTH_LIMIT = SCREEN_WIDTH * 0.9
GAME_HEIGHT_LIMIT = SCREEN_HEIGHT * 0.9

game_on = True


def end_game():
    global game_on
    game_on = False


def onkey_up():
    if game_on and paddle_right.ycor() < SCREEN_HEIGHT/2 - paddle_right.height:
        paddle_right.up()
        screen.update()


def onkey_down():
    if game_on and paddle_right.ycor() > -SCREEN_HEIGHT/2 + paddle_right.height:
        paddle_right.down()
        screen.update()


def onkey_w():
    if game_on and paddle_left.ycor() < SCREEN_HEIGHT/2 - paddle_left.height:
        paddle_left.up()
        screen.update()


def onkey_s():
    if game_on and paddle_left.ycor() > -SCREEN_HEIGHT/2 + paddle_left.height:
        paddle_left.down()
        screen.update()
# Setting up the screen
screen = turtle.Screen()
# game_width_limit = round(screen_width*0.9)
# game_height_limit = round(screen_height*0.9)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()
screen.onkeypress(end_game, "Escape")
screen.onkeypress(onkey_up, "Up")
screen.onkeypress(onkey_down, "Down")
screen.onkeypress(onkey_w, "w")
screen.onkeypress(onkey_s, "s")

# Setting up the paddle
paddle_right = paddle.Paddle(pos=(SCREEN_WIDTH/2*0.9, 0))
paddle_left = paddle.Paddle(pos=(-SCREEN_WIDTH/2*0.9, 0))

# Rolling the ball
ball = ball.Ball(game_width_limit=GAME_WIDTH_LIMIT, game_height_limit=GAME_HEIGHT_LIMIT)

# Setting up the scoreboard
score_board = scoreboard.ScoreBoard(SCREEN_HEIGHT)

while game_on:
    ball.move()

    # On collision with upper and lower walls
    if abs(ball.ycor()) >= GAME_HEIGHT_LIMIT/2:
        ball.ydir *= -1

    # Collision with right paddle
    if ball.xcor() >= paddle_right.xcor() - paddle_right.width / 2 - ball.ball_size / 2:  # Reached x-limit
        if paddle_right.ycor() - paddle_right.height / 2 \
                <= ball.ycor() <= \
                paddle_right.ycor() + paddle_right.height / 2:
            # Should bounce back into the game
            ball.xdir *= -1
        elif paddle_right.height / 2 \
                < abs(ball.ycor() - paddle_right.ycor()) < \
                paddle_right.height / 2 + ball.ball_size:
            # Should bounce out of the game
            ball.ydir *= -1

    # Collision with left paddle
    if ball.xcor() <= paddle_left.xcor() + paddle_left.width / 2 + ball.ball_size / 2:  # Reached x-limit
        if paddle_left.ycor() - paddle_left.height / 2 <= ball.ycor() <= paddle_left.ycor() + paddle_left.height / 2:
            # Should bounce back into the game
            ball.xdir *= -1
        elif paddle_left.height / 2 \
                < abs(ball.ycor() - paddle_left.ycor()) < \
                paddle_left.height / 2 + ball.ball_size:
            # Should bounce out of the game
            ball.ydir *= -1

    # Ball escaped game limits
    if abs(ball.xcor()) >= SCREEN_WIDTH/2:
        if ball.xcor() < 0:
            score_board.score_right()
        else:
            score_board.score_left()
        print("goal")
        ball.goto(0, 0)
        screen.update()
        time.sleep(1)
        ball.xdir *= -1

    screen.update()
    time.sleep(0.01)

screen.exitonclick()
