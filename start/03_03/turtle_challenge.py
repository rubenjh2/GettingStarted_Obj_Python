"""
Chapter 3 challenge.
The world is your Turtle! 
"""
import turtle as t
import numpy as np
import colorsys
import random

# choose the number of racers
players = 10

# setup screen
screen = t.Screen()
screen.setup(0.5, 0.5, None, None)
screen.title("Turtle Race")

turtles = []

# allow for HSL coloring
t.colormode(255)

# get equally spaced starting locations
y_pos = np.linspace(-200, 200, players)

# setup for race
for i in range(players):
    turtle = t.Turtle()
    # move to starting location
    turtle.teleport(-450, y_pos[i])

    turtle.shape("turtle")
    # Hide trail
    turtle.penup()
    turtle.speed(20)

    # setting unique color per turtle
    hue = i / players
    r, g, b = [int(255 * c) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
    turtle.color((r, g, b))

    turtles.append(turtle)

# if any turtle hits x_pos = 430, stop the race
while all(player.position()[0] < 430 for player in turtles):

    for j in range(players):
        move = random.randint(0, 40)
        turtles[j].fd(move)


t.done()
