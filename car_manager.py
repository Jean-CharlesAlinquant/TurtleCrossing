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


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            start_y = random.randint(BOTTOM, TOP)
            new_car.goto(300, start_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.car_list.remove(car)

    def accelerate(self):
        self.car_speed += MOVE_INCREMENT
