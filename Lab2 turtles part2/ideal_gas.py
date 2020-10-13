import turtle as tr
from random import randint
import numpy as np
tr.hideturtle()
tr.penup()
tr.goto(-200,-200)
tr.pendown()
tr.left(180)

for i in range(4):
    tr.right(90)
    tr.fd(400)
tr.penup()

vx = 1
vy = 1

number_of_turtles = 8
tr.turtles()
pool = [tr.Turtle(visible=False) for i in range(number_of_turtles)]
poolx = []
pooly = []
poolalpha = []
poolvx = []
poolvy = []
for unit in pool:
    alpha = randint(1,360)
    x = randint(-200, 200)
    y = randint(-200, 200)

    poolx.append(x)
    pooly.append(y)
    poolvx.append(np.cos((90 - alpha)*np.pi / 180))
    poolvy.append(np.sin((90 - alpha) * np.pi / 180))

    unit.shape('circle')
    unit.speed('fastest')
    unit.turtlesize(0.5)
    unit.penup()
    unit.hideturtle()
    unit.goto(x, y)
    unit.showturtle()

def move(i):
    if poolx[i] >= 200 or poolx[i] <= -200:
        poolvx[i] = -poolvx[i]
    if pooly[i] >= 200 or pooly[i] <= -200:
        poolvy[i] = -poolvy[i]
    poolx[i] += poolvx[i]
    pooly[i] += poolvy[i]
    pool[i].goto(poolx[i], pooly[i])

while True:
    for i in range(number_of_turtles):
        move(i)



tr.exitonclick()
