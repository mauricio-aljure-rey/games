import turtle
import time

class Snake():
    def __init__(self, snake_parts_size=20):
        self.snake_parts = []
        self.snake_parts_size = snake_parts_size
        self.initialize()

    def initialize(self):
        for num_part in range(3):
            self.extend_snake((-num_part * self.snake_parts_size, 0))

    def extend_snake(self, pos):
        new_part = turtle.Turtle()
        new_part.penup()
        new_part.color("white")
        new_part.shape("square")
        new_part.setpos(pos)
        new_part.speed("fastest")
        new_part.resizemode("user")
        new_part.shapesize(round(self.snake_parts_size / 20), round(self.snake_parts_size / 20), 10)
        self.snake_parts.append(new_part)

    def move(self):
        for part_num in reversed(range(1, len(self.snake_parts))):
            self.snake_parts[part_num].setpos(self.snake_parts[part_num - 1].position())
        self.snake_parts[0].forward(self.snake_parts_size)

    def up(self):
        if self.snake_parts[0].heading() != 270:
            self.snake_parts[0].setheading(90)
            self.move()

    def down(self):
        if self.snake_parts[0].heading() != 90:
            self.snake_parts[0].setheading(270)
            self.move()

    def right(self):
        if self.snake_parts[0].heading() != 180:
            self.snake_parts[0].setheading(0)
            self.move()

    def left(self):
        if self.snake_parts[0].heading() != 0:
            self.snake_parts[0].setheading(180)
            self.move()
