import turtle as tr

tr.shape('circle')
tr.turtlesize(1)
tr.width(2)
tr.penup()
tr.hideturtle()
tr.goto(-200, 0)
tr.pendown()
tr.fd(705)
tr.penup()
tr.hideturtle()
tr.goto(-200, 0)
tr.showturtle()
tr.pendown()
Vx = 60 # скорость по иксу
Vyk = 300 # скорость по ординате
ay = -100 # ускорение
dt = 0.01
x = -200
y = 0
for i in range(10):
    y = 0
    Vy = Vyk
    ay *= 1.5
    while y >= 0:
        tr.goto(x, y)
        x += Vx * dt
        y += Vy * dt + ay * dt ** 2/2
        Vy += ay * dt
tr.exitonclick()
