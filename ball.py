#creation and movement of ball

from turtle import Turtle

class ball_class(Turtle):
    #ball creation
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid= 0.5 , stretch_len= 0.5)
        self.ball_x_move = 10 #x_co-ordinate of movement of ball
        self.ball_y_move = 10 #y_co-ordinate of movement of ball

    #ball movement
    def ball_movement(self):
        self.ball_x = self.xcor()+ self.ball_x_move #x_cor + 10
        self.ball_y = self.ycor()+ self.ball_y_move #y_cor + 10
        self.goto(self.ball_x,self.ball_y)

    #ball bouncing of wall
    def wall_bounce(self):
        #ball bounce for wall
        #change the y_co-ordinate of movement of ball to reverse its direction
        self.ball_y_move *= -1

    #ball bouncing of paddle
    def paddle_bounce(self):
        #bouncing paddle of paddle
        #chenge x_cor of movement of ball to reverse its direction
        self.ball_x_move *= -1

    #ball reset to home position and reversing direction(in favour of those who scored)
    def ball_reset(self):
        self.goto(0,0)
        self.ball_x_move *= -1
        self.ball_y_move *= -1