'''
Topics to be Covered:
- Turtle Graphics documentation
- Tuples
- Importing Modules
'''

# # # from turtle import Turtle, Screen

# # # timmy = Turtle()
# # # # timmy.shape("turtle")       # Some methods to use from the documentation
# # # # timmy.color("red")
# # # # timmy.forward(100)
# # # # timmy.backward(30)
# # # # timmy.right(90)

# # # # Draw a square by turtle

# # # for _ in range(4):
# # #     timmy.forward(100)
# # #     timmy.left(90)

# # # screen = Screen()
# # # screen.exitonclick()

# # # # Types of import and then create object from it

# # # # 1. import turtle
# # # #    tim = turtle.Turtle()

# # # # 2. from turtle import Turtle
# # # #    tim = Turtle()

# # # # 3. from turtle import * (To import everythong in turtle)

# # # # Aliasing Module
# # # # import turtle as t
# # # # tom = t.Turtle()

# # # # Draw dashed line

# # # tom = Turtle()
# # # for i in range(15):
# # #     tom.forward(10)
# # #     tom.penup()
# # #     tom.forward(10)
# # #     tom.pendown()

# # # screen = Screen()
# # # screen.exitonclick()

# # # Drawing different shapes with different colour

# # from turtle import Turtle, Screen
# # import random

# # tan = Turtle()

# # colours = ["red","orange","yellow","green","blue","indigo","purple"]

# # def shape(sides):
# #     angle = 360 / sides
# #     for i in range(sides):
# #         tan.forward(100)
# #         tan.right(angle)

# # for side_shape in range(3,11):
# #     tan.color(random.choice(colours))
# #     shape(side_shape)

# # screen = Screen()
# # screen.exitonclick()

# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color

# directions = [0, 90, 180, 270]
# tim.speed("fastest")
# tim.pensize(15)

# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# Spirograph
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

tim.speed("fastest")

for i in range(100):
    tim.circle(100)
    tim.color(random_color())
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

screen = t.Screen()
screen.exitonclick()