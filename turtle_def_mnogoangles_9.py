import turtle as tr
import numpy as np
import math
tr.shape('turtle')
tr.speed(10)
tr.color('green')
tr.width(1)
a = 30
def angle(n):
    return 180 - (180 * (n - 2) / n)
def mnogoangle(a, n):
    return a / (2 * np.sin(180 / n))


r1 = a/(2*math.sin(np.pi/(3))) #радиус описанной окружности 1
r2 = 0 #радиус описанной окружности 2
aa = 30
for n in range(3, 10):
    tr.penup()
    r2 = a / (2 * math.sin(np.pi / n))
    if n == 4:
        tr.goto((aa - a) / 2, -7.5)
    else:
        tr.goto((aa - a) / 2, (r1 - r2))
    tr.fd(a)
    tr.pendown()
    for j in range(n):
        tr.left(angle(n))
        tr.fd(a)
    a += 10
tr.exitonclick()
