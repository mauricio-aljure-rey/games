import turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100 # Used to calculate number of turtles


class Paddle(turtle.Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setpos(pos)
        self.speed("fastest")
        self.resizemode("user")
        self.setheading(90)
        self.height = PADDLE_HEIGHT
        self.width = PADDLE_WIDTH
        self.shapesize(stretch_wid=(PADDLE_WIDTH/20), stretch_len=(PADDLE_HEIGHT/20))

    def up(self):
        self.setheading(90)
        self.forward(PADDLE_WIDTH)

    def down(self):
        self.setheading(270)
        self.forward(PADDLE_WIDTH)

