import time
from turtle import Turtle , Screen
from paddle import paddles
from ball import ball_class
from score import scoreboard


#setting up ball speed
ball_speed = 0.1
#creating ball object
ball = ball_class()

#creating paddle object
paddle_right = paddles(330 , 0)
paddle_left = paddles(-330 , 0)

#creating score objects
score = scoreboard()


#setting up screen
screen = Screen()
screen.setup(width= 700 , height= 500)
screen.bgcolor("black")
screen.title("PONG...")
screen.tracer(0)

#for assigning keys
screen.listen()

#assigning keys for right paddle
screen.onkey(paddle_right.paddle_move_up , "o")
screen.onkey(paddle_right.paddle_move_down , "l")

#assigning keys for left paddle
screen.onkey(paddle_left.paddle_move_up , "u")
screen.onkey(paddle_left.paddle_move_down , "s")



is_game_on = True

while is_game_on:
    time.sleep(ball_speed)
    screen.update()
    ball.ball_movement()

    #detect collision with wall
    if ball.ball_y > 230 or ball.ball_y < -230:
        ball.wall_bounce()

    #detect collision with right paddle
    if ball.xcor() > 300 and ball.distance(paddle_right)<50:
        ball.paddle_bounce()
    #detect collision with left paddle
    if ball.xcor() < -300 and ball.distance(paddle_left)<50:
        ball.paddle_bounce()
        ball_speed *= 0.7

    #detect when paddle misses
    if ball.xcor() > 330:
        #giving point to right
        score.inc_l_score()
        #reset
        ball.ball_reset()
    elif ball.xcor() < -330:
        score.inc_r_score()
        ball.ball_reset()
        ball_speed = 0.1

    #give winner
    if score.l_score == 5 or score.r_score == 5:
        is_game_on = False
        score.winner()









screen.exitonclick()