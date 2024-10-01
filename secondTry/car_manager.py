from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

CAR_LANES = []
for i in range (0, 12):
    new_car_lane = ( (40 * i) - 220)
    CAR_LANES.append(new_car_lane)


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            #random_y = random.randint(-240, 250)
            new_car.goto(300, random.choice(CAR_LANES))
            self.all_cars.append(new_car)

    def move_cars(self, playersLevel):

        print(playersLevel)

        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * playersLevel))

            print(f"speed = {STARTING_MOVE_DISTANCE + (playersLevel)}")