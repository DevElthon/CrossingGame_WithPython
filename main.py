import time
from turtle import Screen, Turtle
from player import Player
from  scoreboard import  ScoreBoard
from car_manager import CarManager

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Crossing Turtle")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()