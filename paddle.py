from turtle import Turtle, Screen



class Paddle(Turtle):
    def __init__(self,initial_pos):
        super().__init__()
        # self.paddle = Turtle("square")
        self.paddle_list = []
        self.color("white")
        self.penup()
        self.hideturtle()
        for position in initial_pos:
            pp = Turtle("square")
            pp.color('white')
            pp.penup()
            self.paddle_list.append(pp)
            pp.goto(position)

    def move_up(self):
        x = self.paddle_list[0].xcor()
        y = self.paddle_list[0].ycor()
        self.paddle_list[1].goto(x, y)
        self.paddle_list[0].setheading(90)
        self.paddle_list[0].fd(20)
    def move_down(self):
        x = self.paddle_list[0].xcor()
        y = self.paddle_list[0].ycor()
        self.paddle_list[1].goto(x, y)
        self.paddle_list[0].setheading(270)
        self.paddle_list[0].fd(20)


