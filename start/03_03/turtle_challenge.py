"""
Chapter 3 challenge.
The world is your Turtle! 
"""
import turtle as t
import numpy as np

# choose the number of racers
players = 5

# setup screen
screen = t.Screen()
screen.setup(0.5, 0.5, None, None)
screen.title("Turtle Race")


turtles = []
# create turtle object for each player
for i in range(players):
    turtle = t.Turtle()
    turtles.append(turtle)

y_pos = np.linspace(-200, 200, players)

# allow for HSL coloring
turtle.colormode(255)
# CONTINUE WITH SETTING UNIQUE COLORS PER PLAYER

for j in range(players):
    turtles[j].teleport(-450, y_pos[j])

    # setting unique color per turtle
    turtles[j].color("blue")
    print(turtles[j].position())


# # turtle1.fd(-250)
# # print(turtle1.position())


t.done()
