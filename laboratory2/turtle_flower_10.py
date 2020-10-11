import turtle as tr
import numpy as np
tr.shape('turtle')
tr.speed(6)
tr.color('red')


n = int(input('Введите кол-во лепестков '))
angle = 360 / n
for n in range(n):
    tr.turtlesize(1)
    tr.circle(60)
    tr.right(angle)
tr.exitonclick()