import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Variables
FINISH_LINE_Y = 265
Level = 0

# New objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Screen settings
screen.listen()
screen.onkey(player.up, "Up")


def new_level():
    player.hideturtle()
    player.goto(player.start)
    player.showturtle()
    game_is_on = True
    while game_is_on:
        global Level

        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars(Level)

        for car in range(0, len(car_manager.all_cars)):
            if car_manager.all_cars[car].distance(player) < 25:
                game_is_on = False
                scoreboard.game_over()
                return False

        if FINISH_LINE_Y <= player.ycor():
            game_is_on = False
            scoreboard.new_point()
            Level += 1


player_is_alive = True
while player_is_alive:
    if new_level() == False:
        player_is_alive = False

screen.exitonclick()
"""
    counter = 0
    for car in car_manager.all_cars:
        print(car_manager.all_cars[counter].distance(player))
        counter += 1
"""
