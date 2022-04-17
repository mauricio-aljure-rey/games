import turtle

BALL_SIZE = 20


class Ball(turtle.Turtle):
    def __init__(self, game_height_limit, game_width_limit):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ball_size = BALL_SIZE
        self.shapesize(round(BALL_SIZE / 20), round(BALL_SIZE / 20), 0)
        self.speed("fastest")
        self.xdir = 2
        self.ydir = 2

    def move(self):
        self.goto((self.xcor() + self.xdir, self.ycor() + self.ydir))
