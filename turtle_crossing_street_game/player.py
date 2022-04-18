import turtle


class Player(turtle.Turtle):
    def __init__(self, game_height_limit, lines_size):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("aquamarine4")
        self.shape_factor = 0.6
        self.shapesize(lines_size/20 * self.shape_factor, lines_size/20 * self.shape_factor, 0)
        self.speed("fastest")
        self.turtle_step = lines_size
        self.setheading(90)
        self.init_y = -game_height_limit/2 - lines_size
        self.goto(0, self.init_y)
        self.player_released = False
        self.delay_counter = 0

    def move_up(self):
        self.forward(self.turtle_step)

    def init_pos(self):
        self.goto(0, self.init_y)
