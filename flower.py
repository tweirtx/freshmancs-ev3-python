import turtle
from random import randint

turtlepointer = turtle.Pen()


def petal(radius):
    heading = turtlepointer.heading()
    turtlepointer.circle(radius, 60)
    turtlepointer.left(120)
    turtlepointer.circle(radius, 60)
    turtlepointer.setheading(heading)


def draw():
    radius = randint(30, 100)
    petals = randint(3, 8)
    degrees = 360 / petals
    petals += 1
    for i in range(petals):
        petal(radius)
        turtlepointer.setheading(degrees * i)


colors = ['red', 'green', 'blue']
while True:
    turtlepointer.color(colors[randint(0, 2)])
    draw()
    turtlepointer.penup()
    turtlepointer.setx(randint(-50, 100))
    turtlepointer.sety(randint(-50, 100))
    turtlepointer.pendown()
