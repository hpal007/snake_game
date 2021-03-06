from turtle import Turtle

# variables
CHANCE = 3
ALIGNMENT = 'center'
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.chance_left = CHANCE
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}  High Score: {self.high_score} Chance Left: {self.chance_left}',
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER !!! ', align=ALIGNMENT, font=FONT)
