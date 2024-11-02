
from turtle import Turtle

LIST_OF_STARTING_SEGMENT = [(0,0),(-20,0),(-40,0)]
DISTENCE = 20
LEFT = 180
RIGHT = 0
DOWN = 270
UP = 90

# creates the body of the snake & control the movement of the snake.
class Snake:
        def __init__(self):
            self.segments = []
            self.create_snake()
            self.head = self.segments[0]
           
            
        def create_snake(self):
              for position in LIST_OF_STARTING_SEGMENT:
                   self.add_segment(position)
              

        def add_segment(self,position):
                new_segment = Turtle()
                new_segment.penup()
                new_segment.shape("square")
                new_segment.color("white")
                new_segment.goto(position)
                self.segments.append(new_segment)


        def extend_snake(self):
             self.add_segment(self.segments[-1].position())


        def move(self):               
            for seg_num in range(len(self.segments)-1,0,-1): 
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x,new_y)

            self.head.forward(DISTENCE)

        def up(self):
             if self.head.heading() != DOWN:
                self.head.setheading(UP)  

        def down(self):
             if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def left(self):
             if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        def right(self):
             if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)