import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your Bet", "Which turtle would win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
a = 100
all_turtles = []

for x in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(-230, a)
    a -= 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()