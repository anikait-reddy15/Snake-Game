from turtle import Turtle

alignment = 'center'
font = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def score_increase(self):
        self.score += 1
        self.clear()
        self.home()
        self.goto(0, 260)
        self.write(f"Score : {self.score}", True, align= alignment, font= font)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", True, align= alignment, font= font)

    def game_over(self):
        self.goto(0, 0)
        self.write("Get better!!", True, align = alignment, font= font)
