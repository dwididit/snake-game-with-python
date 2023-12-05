from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("YOU LOSE!", align="center", font=("Arial", 24, "normal"))


    def win(self):
        self.penup()
        self.goto(0,0)
        self.write("YOU WIN", align="center", font=("Arial", 24, "normal"))