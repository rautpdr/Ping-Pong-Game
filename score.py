#counting and updating score

from turtle import Turtle

class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    #update score
    def update_score(self):
        self.clear() #clear old score
        self.goto(-200,210)
        self.write(self.l_score , False , "center" ,("Arial" , 24 , "bold"))
        self.goto(200,210)
        self.write(self.r_score , False , "center" ,("Arial" , 24 , "bold"))

    def inc_l_score(self):
        self.l_score += 1
        self.update_score()

    def inc_r_score(self):
        self.r_score += 1
        self.update_score()


    #winner is the one who reaches 5 points
    def winner(self):
        self.goto(0,0)
        self.write("Winner has been Decided!" , False , "center" ,("Arial" , 20 , "bold"))



