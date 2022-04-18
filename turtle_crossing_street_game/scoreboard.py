import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self, game_height_limit, lines_size):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, round(game_height_limit/2 + lines_size))
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 16))

    def score_up(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.clear()
        self.write(f'GAME OVER. Score: {self.score}', move=False, align='center', font=('Arial', 16))
