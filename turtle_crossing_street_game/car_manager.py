import turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
CARS_STEP = 5
CAR_WIDTH_FACTOR = 2  # Times the lines_size
SPEED_UP = 2
CAR_DELAY_FACTOR = 2


class CarManager:
    def __init__(self, lines_size, game_height_limit, screen_width):
        self.car_list = []
        self.car_width = lines_size * CAR_WIDTH_FACTOR
        self.car_height = lines_size * 0.9
        self.lines_size = lines_size
        self.game_height_limit = game_height_limit
        self.screen_width = screen_width
        self.cars_step_ini = CARS_STEP
        self.cars_step = CARS_STEP
        self.car_delay_min = self.car_width / self.cars_step
        self.car_delay = self.car_delay_min * CAR_DELAY_FACTOR
        self.car_delay_counter = 0

    def produce_car(self):
        self.car_delay_counter += 1
        if self.car_delay_counter >= self.car_delay:
            self.car_delay_counter = 0
            new_car = turtle.Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.speed("fastest")
            new_car.resizemode("user")
            new_car.shapesize(stretch_wid=(self.car_height / 20), stretch_len=(self.car_width / 20), outline=0)
            new_car.color(random.choice(COLORS))
            # Checking that it is not produced on top of another car
            check_flag = True
            while check_flag:
                check_flag = False
                y_pos = self.lines_size * round(self.game_height_limit * (random.random() - 1 / 2) / self.lines_size)
                if self.car_list:  # In case there are no cars in the list
                    for car in self.car_list:
                        if car.ycor() == y_pos:
                            if car.xcor() < -self.screen_width / 2 + self.car_width * 2:
                                check_flag = True
                else:
                    check_flag = False
            new_car.setpos((-self.screen_width / 2, y_pos))
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.cars_step)

    def update_cars(self):
        self.produce_car()
        self.move_cars()
        self.delete_cars()

    def delete_cars(self):
        for idx, car in enumerate(self.car_list):
            if car.xcor() > self.screen_width / 2 * 1.2:
                car.backward(self.cars_step)
                car.ht()
                self.car_list.pop(idx)

    def increase_speed(self):
        self.cars_step += SPEED_UP
        self.car_delay /= (round(SPEED_UP)/1.5)
