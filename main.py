from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball

INITIAL_POS = {1:[(320,10),(320,-10)], 2: [(-320,10),(-320,-10)]}

screen = Screen()
screen.bgcolor("black")
screen.screensize(600,600)
screen.listen()
screen.tracer(0)


def draw_dashed_line(t_obj):
    t_obj.color("white")
    t_obj.hideturtle()
    t_obj.penup()
    t_obj.goto(0,-300)
    t_obj.left(90)
    for i in range(38):
        t_obj.fd(8)
        t_obj.penup()
        t_obj.fd(8)
        t_obj.pendown()


#draw right paddle
p1 = Paddle(INITIAL_POS[1])
p2 = Paddle(INITIAL_POS[2])
ball = Ball()


screen.onkeypress(p1.move_up,"Up")
screen.onkeypress(p1.move_down,"Down")
screen.onkeypress(p2.move_up, "e")
screen.onkeypress(p2.move_down, 'd')


draw_dashed_line(Turtle())

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.xcor() > 300 or ball.xcor()<-300:
        is_game_on = False







screen.exitonclick()