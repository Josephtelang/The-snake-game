from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh() # it is used to refresh the food at the inital position.
      

    def refresh(self):
        self.random_x = random.randint(-275,275)
        self.random_y = random.randint(-275,275)
        self.goto(self.random_x,self.random_y)
