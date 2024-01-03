import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
KEY_UP = "Up"
TITLE = "Turtle Crossing"

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title(TITLE)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up, KEY_UP)

loop = 0
car_list = []
game_is_on = True
while game_is_on:
    loop += 1
    time.sleep(0.1)
    screen.update()
    if loop % 6 == 0:
        car = CarManager()
        car_list.append(car)

    for car in car_list:
        car.move()

    # Detect collision between turtle and car
