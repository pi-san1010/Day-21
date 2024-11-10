from turtle import Turtle,Screen
import random


ANGLE_LIST = list(range(0,360,10))
INIT_POSY = [-180,-120,-60,0,60,120,180]

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.ball = Turtle("circle")
		self.ball.penup()
		self.initial_position = (0,random.choice(INIT_POSY))
		self.ball.goto(self.initial_position)
		self.ball.color("green")
		self.ball.setheading(random.choice(ANGLE_LIST))

	def move(self):		
		self.ball.fd(20)
