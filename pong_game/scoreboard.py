import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score_left_counter = 0
        self.score_right_counter = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, round(screen_height/2*0.9))
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Score {self.score_left_counter}:{self.score_right_counter}',
                   move=False, align='center', font=('Arial', 16))

    def score_left(self):
        self.score_left_counter += 1
        self.refresh()

    def score_right(self):
        self.score_right_counter += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', move=False, align='center', font=('Arial', 16))

