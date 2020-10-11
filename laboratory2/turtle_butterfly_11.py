import turtle as tr
import numpy as np
tr.shape('turtle')
tr.speed(6)
tr.color('black')
radius = 20
tr.right(90)
for n in range(10):
    tr.turtlesize(1)
    tr.circle(radius)
    tr.right(180)
    tr.circle(radius)
    tr.right(180)
    radius += 10
tr.exitonclick()
