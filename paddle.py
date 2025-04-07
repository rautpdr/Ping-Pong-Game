#creattion and movement of paddles
from turtle import Turtle



class paddles(Turtle):
    #paddle creation
    def __init__(self, x_co_ordinate , y_co_ordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len= 0.5 , stretch_wid= 4)
        self.goto(x_co_ordinate , y_co_ordinate)



    #paddle movement
    def paddle_move_up(self):
        up = self.ycor() + 10  # getting y-coordinate of paddle
        self.goto(self.xcor() , up)


    def paddle_move_down(self):
        down = self.ycor() - 10  # getting y-coordinate of paddle
        self.goto(self.xcor() , down)




