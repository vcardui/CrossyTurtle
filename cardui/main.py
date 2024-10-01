import threading
import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# New objects
squirt = Player()
allCars = []
for i in range(0, 13):
    newCar = CarManager(i)
    allCars.append(newCar)

# Screen settings
screen.listen()
screen.onkey(squirt.up, "Up")

allCarThreads = []
for item in allCars:
    randTime = random.randint(0, 5)
    print(f"randTime = {randTime}")
    print("BEFORE create CarThread")
    CarThread = threading.Timer(randTime, item.move, args=None, kwargs=None)
    print("AFTER create CarThread")
    allCarThreads.append(CarThread)

for car in allCarThreads:
    print("BEFORE start CarThread")
    car.start()
    print("AFTER start CarThread")
    screen.update()


def move_cars():
    for itemCar in allCars:
        if itemCar.xcor() <= -320:
            itemCar.setx(320)
        # elif 320 <= item.xcor():
        else:
            print(itemCar.xcor())
            itemCar.move()

# waitTime = random.randint(0, 7)
# t = Timer(10, allCars[0].move())
# t.start()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for itemCar in allCars:
        if (itemCar.distance(squirt) < 25) or (itemCar.distance(squirt) < 25):
            print("I hit the turtle")
        else:
            for itemCar in allCars:
                itemCar.move()

    # move_cars()

screen.exitonclick()
