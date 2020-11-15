import turtle as tr
from random import randint
import numpy as np

tr.hideturtle()
tr.penup()
tr.goto(-200,-200)
tr.pendown()


tr.left(180)
x = randint(-200, 200)
y = randint(-200, 200)
vx = 1
vy = 1
for i in range(4):
    tr.right(90)
    tr.fd(400)
tr.penup()
tr.goto(x, y)
tr.showturtle()
alpha = randint(1, 90)
shag = 1
tr.shape('circle')
tr.right(90)
tr.right(alpha)



while True:
    if x >= 200 or x <= -200:
        vx = -vx
    if y >= 200 or y <= -200:
        vy = -vy
    x += np.cos((90 - alpha)*np.pi / 180) * vx
    y += np.sin((90 - alpha) * np.pi / 180) * vy
    tr.goto(x, y)



tr.exitonclick()
