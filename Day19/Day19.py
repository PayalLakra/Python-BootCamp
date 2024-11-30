'''
Topics to be covered:
- Python Higher Order Functions and Event Listeners
- Object state and Instances
- Turtle Coordinate system
'''

# from turtle import Turtle, Screen

# tammy = Turtle()
# screen= Screen()

# def move_forward():
#     tammy.forward(10)

# screen.listen()
# screen.onkey(key='space', fun=move_forward)   # Here it is used as higher order fucntion as it works with other function
# screen.exitonclick()   # On pressing space only then turtle moves

# Etch-A-Sketch
# W = Forward
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear Drawing

# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forward, "w")   # Here it is used as higher order fucntion as it works with other function
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a") 
# screen.onkey(turn_right, "d") 
# screen.onkey(clear, "c")
# screen.exitonclick()

# Object State and Instances
tammy.color = green
tim.colour = blue  # so these are 2 diff. states of objects from same class

# Turtle Race
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)  # Screen size
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Setting up the turtles at the starting line
for turtle_index in range(6):
    tim = Turtle()
    tim.color(colors[turtle_index])
    tim.penup()
    tim.shape("turtle")
    tim.goto(x=-230, y=y_positions[turtle_index])  # Adjusting the y-positions
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Move each turtle a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! The {winning_color} turtle won, and so did you!")
            else:
                print(f"Sorry, the {winning_color} turtle won. Better luck next time!")

screen.exitonclick()  # Hold the screen until a click