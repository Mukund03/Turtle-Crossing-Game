import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player1.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_left()

    for car in cars.all_cars:
        if car.distance(player1) < 20:
            game_is_on = False
            score.game_over()

    if player1.on_finish_line():
        player1.go_to_start()
        cars.level_up()
        score.level_up()


screen.exitonclick()
