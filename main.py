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
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, KEY_UP)

loop = 0
car_list = []
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision between turtle and car
    for car in car_manager.car_list:
        if (player.distance(car)) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when turtle reaches finish line
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.accelerate()
        scoreboard.level_up()


screen.exitonclick()
