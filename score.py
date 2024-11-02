from turtle import Turtle
FONT = ("arial",15,"normal")
ALIGNMENT = "center"

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,279)
        self.update_score()

    def update_score(self):
        self.write(arg=f"score : {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="game over",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        


