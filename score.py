from turtle import Turtle
FONT = ("arial",15,"normal")
ALIGNMENT = "center"

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt","r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0,279)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"score : {self.score} High Score: {self.highscore}",align=ALIGNMENT,font=FONT)
        
    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open("data.txt","w") as file :
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
            
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="game over",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
        


