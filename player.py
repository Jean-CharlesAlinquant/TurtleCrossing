from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

# Create a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle north


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_position()
        self.setheading(UP)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False