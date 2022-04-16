import turtle
import random
import time

class Food(turtle.Turtle):
    def __init__(self, game_height_limit, game_width_limit, snake_parts_size, food_size, snake):
        super().__init__()
        # TODO: change shappe to an apple. A giff file must be imported.
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.food_size = food_size
        self.shapesize(round(self.food_size/20), round(self.food_size/20), 12)
        self.speed("fastest")
        self.game_height_limit = game_height_limit
        self.game_width_limit = game_width_limit
        self.snake_parts_size = snake_parts_size
        self.move(snake)

    def move(self, snake):
        repeat_again = False
        while True:
            x_pos = random.randint(-(self.game_width_limit - self.food_size) / 2,
                                   (self.game_width_limit - self.food_size)/2)
            y_pos = random.randint(-(self.game_height_limit - self.food_size) / 2,
                                   (self.game_height_limit - self.food_size)/2)
            x_pos_rounded = self.snake_parts_size * round(x_pos / self.snake_parts_size)
            y_pos_rounded = self.snake_parts_size * round(y_pos / self.snake_parts_size)
            for part in snake.snake_parts:
                if part.distance((x_pos_rounded, y_pos_rounded)) < self.food_size * 1.2:
                    # Break only if the distance is larger. Else, iterate again.
                    repeat_again = True
            if repeat_again is False:
                break
            else:
                repeat_again = False

        self.goto(x_pos_rounded, y_pos_rounded)
