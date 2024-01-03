from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TOP = 250
BOTTOM = -250

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and move to the left edge of the screen.
# No cars should be generated in the top and bottom 50px of the screen
# (think of it as a safe zone for our little turtle).


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        color = random.choice(COLORS)
        self.color(color)
        self.penup()
        self.shapesize(1, 2)
        start_y = random.randint(BOTTOM, TOP)
        self.goto(250, start_y)

    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())


